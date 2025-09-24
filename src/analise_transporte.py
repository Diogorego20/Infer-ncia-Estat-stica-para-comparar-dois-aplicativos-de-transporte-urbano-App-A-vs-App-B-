#!/usr/bin/env python3
"""
Análise Estatística Completa - Transporte Urbano (Apps A vs B)

Este módulo implementa análise estatística comparativa entre dois aplicativos
de transporte urbano, utilizando técnicas de inferência estatística para
avaliar performance operacional e satisfação do usuário.

Autor: Diogo Da Silva Rego
Disciplina: Inferência Estatística I - UFPB CCEN
Matrícula: 20240045381
Data: 23/09/2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import t, chi2, f, norm
from scipy.stats import gaussian_kde, probplot
import warnings
import os
from pathlib import Path

warnings.filterwarnings('ignore')

# Configuração para visualizações
plt.rcParams.update({
    'font.size': 10,
    'figure.figsize': (12, 8),
    'axes.grid': True,
    'grid.alpha': 0.3
})


class AnaliseTransporte:
    """
    Classe principal para análise estatística de aplicativos de transporte.
    
    Esta classe implementa métodos para:
    - Análise descritiva dos dados
    - Cálculo de intervalos de confiança
    - Testes de hipóteses
    - Análise de SLA
    - Geração de visualizações
    
    Attributes:
        dados (pd.DataFrame): DataFrame com os dados de tempo de espera
        app_a (np.array): Dados do aplicativo A
        app_b (np.array): Dados do aplicativo B
        pesquisa (dict): Dados da pesquisa de satisfação
    """
    
    def __init__(self, dados_path: str, output_dir: str = "outputs"):
        """
        Inicializa a análise com os dados de transporte.
        
        Args:
            dados_path (str): Caminho para o arquivo CSV com os dados
            output_dir (str): Diretório para salvar outputs
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Carregar e processar dados
        self.dados = pd.read_csv(dados_path)
        self.dados.columns = ['app', 'espera_min']
        
        # Separar dados por aplicativo
        self.app_a = self.dados[self.dados['app'] == 'A']['espera_min'].values
        self.app_b = self.dados[self.dados['app'] == 'B']['espera_min'].values
        
        # Dados da pesquisa de opinião (conforme especificação do problema)
        self.pesquisa = {
            'A': {'aprovacoes': 132, 'total': 150},
            'B': {'aprovacoes': 120, 'total': 150}
        }
        
        self._log_dados_carregados()
    
    def _log_dados_carregados(self) -> None:
        """Log das informações dos dados carregados."""
        print(f"Dados carregados:")
        print(f"App A: {len(self.app_a)} observações")
        print(f"App B: {len(self.app_b)} observações")
        print(f"Total: {len(self.dados)} observações")
        print(f"Pesquisa: {sum(self.pesquisa[app]['total'] for app in ['A', 'B'])} usuários\n")
    
    def estatisticas_descritivas(self) -> tuple:
        """
        Calcula estatísticas descritivas básicas para ambos os aplicativos.
        
        Returns:
            tuple: (stats_a, stats_b) com dicionários de estatísticas
        """
        def calcular_stats(dados: np.array) -> dict:
            return {
                'n': len(dados),
                'media': np.mean(dados),
                'mediana': np.median(dados),
                'dp': np.std(dados, ddof=1),
                'variancia': np.var(dados, ddof=1),
                'cv': np.std(dados, ddof=1) / np.mean(dados),
                'p90': np.percentile(dados, 90),
                'p95': np.percentile(dados, 95),
                'iqr': np.percentile(dados, 75) - np.percentile(dados, 25),
                'min': np.min(dados),
                'max': np.max(dados)
            }
        
        return calcular_stats(self.app_a), calcular_stats(self.app_b)
    
    def ic_media(self, dados: np.array, confianca: float = 0.95) -> dict:
        """
        Calcula intervalo de confiança para a média usando distribuição t.
        
        Args:
            dados (np.array): Dados da amostra
            confianca (float): Nível de confiança (default: 0.95)
            
        Returns:
            dict: Dicionário com resultados do IC
        """
        n = len(dados)
        media = np.mean(dados)
        dp = np.std(dados, ddof=1)
        se = dp / np.sqrt(n)
        
        alpha = 1 - confianca
        t_crit = t.ppf(1 - alpha/2, df=n-1)
        me = t_crit * se
        
        return {
            'confianca': confianca,
            'n': n,
            'media': media,
            'dp': dp,
            'se': se,
            'margem_erro': me,
            'amplitude': 2 * me,
            'li': media - me,
            'ls': media + me
        }
    
    def ic_diferenca_medias_welch(self, x: np.array, y: np.array, 
                                  confianca: float = 0.95) -> dict:
        """
        Calcula IC para diferença de médias usando teste de Welch.
        
        O teste de Welch não assume variâncias iguais entre os grupos.
        
        Args:
            x (np.array): Dados do primeiro grupo
            y (np.array): Dados do segundo grupo
            confianca (float): Nível de confiança
            
        Returns:
            dict: Resultados do IC para diferença de médias
        """
        n1, n2 = len(x), len(y)
        m1, m2 = np.mean(x), np.mean(y)
        s1, s2 = np.std(x, ddof=1), np.std(y, ddof=1)
        
        diff = m1 - m2
        se = np.sqrt(s1**2/n1 + s2**2/n2)
        
        # Graus de liberdade de Welch-Satterthwaite
        df = (s1**2/n1 + s2**2/n2)**2 / ((s1**2/n1)**2/(n1-1) + (s2**2/n2)**2/(n2-1))
        
        alpha = 1 - confianca
        t_crit = t.ppf(1 - alpha/2, df=df)
        me = t_crit * se
        
        return {
            'confianca': confianca,
            'df': df,
            'diferenca': diff,
            'se': se,
            'margem_erro': me,
            'amplitude': 2 * me,
            'li': diff - me,
            'ls': diff + me
        }
    
    def ic_variancia(self, dados: np.array, confianca: float = 0.95) -> dict:
        """
        Calcula IC para variância usando distribuição qui-quadrado.
        
        Args:
            dados (np.array): Dados da amostra
            confianca (float): Nível de confiança
            
        Returns:
            dict: Resultados do IC para variância
        """
        n = len(dados)
        s2 = np.var(dados, ddof=1)
        
        alpha = 1 - confianca
        chi2_inf = chi2.ppf(alpha/2, df=n-1)
        chi2_sup = chi2.ppf(1 - alpha/2, df=n-1)
        
        li = (n-1) * s2 / chi2_sup
        ls = (n-1) * s2 / chi2_inf
        
        return {
            'confianca': confianca,
            'n': n,
            'variancia': s2,
            'li': li,
            'ls': ls
        }
    
    def ic_razao_variancias(self, x: np.array, y: np.array, 
                           confianca: float = 0.95) -> dict:
        """
        Calcula IC para razão de variâncias usando distribuição F.
        
        Args:
            x (np.array): Dados do primeiro grupo
            y (np.array): Dados do segundo grupo
            confianca (float): Nível de confiança
            
        Returns:
            dict: Resultados do IC para razão de variâncias
        """
        n1, n2 = len(x), len(y)
        s1_2, s2_2 = np.var(x, ddof=1), np.var(y, ddof=1)
        
        razao = s1_2 / s2_2
        
        alpha = 1 - confianca
        f_inf = f.ppf(alpha/2, dfn=n1-1, dfd=n2-1)
        f_sup = f.ppf(1 - alpha/2, dfn=n1-1, dfd=n2-1)
        
        li = razao / f_sup
        ls = razao / f_inf
        
        return {
            'confianca': confianca,
            'df1': n1-1,
            'df2': n2-1,
            'razao': razao,
            'li': li,
            'ls': ls
        }
    
    def ic_proporcao_wald(self, x: int, n: int, confianca: float = 0.95) -> dict:
        """
        Calcula IC para proporção usando método de Wald.
        
        Args:
            x (int): Número de sucessos
            n (int): Tamanho da amostra
            confianca (float): Nível de confiança
            
        Returns:
            dict: Resultados do IC para proporção
        """
        p = x / n
        alpha = 1 - confianca
        z_crit = norm.ppf(1 - alpha/2)
        se = np.sqrt(p * (1-p) / n)
        me = z_crit * se
        
        return {
            'confianca': confianca,
            'x': x,
            'n': n,
            'proporcao': p,
            'se': se,
            'margem_erro': me,
            'amplitude': 2 * me,
            'li': p - me,
            'ls': p + me
        }
    
    def ic_diferenca_proporcoes_wald(self, x1: int, n1: int, x2: int, n2: int,
                                    confianca: float = 0.95) -> dict:
        """
        Calcula IC para diferença de proporções usando método de Wald.
        
        Args:
            x1, n1 (int): Sucessos e tamanho da amostra 1
            x2, n2 (int): Sucessos e tamanho da amostra 2
            confianca (float): Nível de confiança
            
        Returns:
            dict: Resultados do IC para diferença de proporções
        """
        p1, p2 = x1/n1, x2/n2
        diff = p1 - p2
        
        alpha = 1 - confianca
        z_crit = norm.ppf(1 - alpha/2)
        se = np.sqrt(p1*(1-p1)/n1 + p2*(1-p2)/n2)
        me = z_crit * se
        
        return {
            'confianca': confianca,
            'x1': x1, 'n1': n1, 'x2': x2, 'n2': n2,
            'diferenca': diff,
            'se': se,
            'margem_erro': me,
            'amplitude': 2 * me,
            'li': diff - me,
            'ls': diff + me
        }
    
    def calcular_sla(self, dados: np.array, limite: float = 5) -> float:
        """
        Calcula SLA (Service Level Agreement) - % de atendimentos dentro do limite.
        
        Args:
            dados (np.array): Dados de tempo de espera
            limite (float): Limite de tempo em minutos
            
        Returns:
            float: Proporção de atendimentos dentro do limite
        """
        return np.mean(dados <= limite)
    
    def gerar_visualizacoes(self) -> None:
        """Gera visualizações dos dados e salva no diretório de output."""
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        
        # Boxplot
        self.dados.boxplot(column='espera_min', by='app', ax=axes[0,0])
        axes[0,0].set_title('Tempo de Espera por Aplicativo')
        axes[0,0].set_xlabel('Aplicativo')
        axes[0,0].set_ylabel('Tempo de Espera (min)')
        
        # Histogramas
        axes[0,1].hist(self.app_a, alpha=0.7, label='App A', bins=15, density=True)
        axes[0,1].hist(self.app_b, alpha=0.7, label='App B', bins=15, density=True)
        axes[0,1].set_title('Distribuição dos Tempos de Espera')
        axes[0,1].set_xlabel('Tempo de Espera (min)')
        axes[0,1].set_ylabel('Densidade')
        axes[0,1].legend()
        
        # Curvas de densidade
        x_range = np.linspace(min(min(self.app_a), min(self.app_b)), 
                             max(max(self.app_a), max(self.app_b)), 100)
        kde_a = gaussian_kde(self.app_a)
        kde_b = gaussian_kde(self.app_b)
        
        axes[1,0].plot(x_range, kde_a(x_range), label='App A', linewidth=2)
        axes[1,0].plot(x_range, kde_b(x_range), label='App B', linewidth=2)
        axes[1,0].fill_between(x_range, kde_a(x_range), alpha=0.3)
        axes[1,0].fill_between(x_range, kde_b(x_range), alpha=0.3)
        axes[1,0].set_title('Curvas de Densidade')
        axes[1,0].set_xlabel('Tempo de Espera (min)')
        axes[1,0].set_ylabel('Densidade')
        axes[1,0].legend()
        
        # Q-Q plot para normalidade
        probplot(self.app_a, dist="norm", plot=axes[1,1])
        axes[1,1].set_title('Q-Q Plot - App A (Teste de Normalidade)')
        
        plt.tight_layout()
        output_path = self.output_dir / 'visualizacoes_transporte.png'
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"Visualizações salvas em: {output_path}")
    
    def executar_analise_completa(self) -> tuple:
        """
        Executa análise estatística completa e gera relatório.
        
        Returns:
            tuple: (stats_a, stats_b) com estatísticas descritivas
        """
        print("="*80)
        print("ANÁLISE ESTATÍSTICA COMPLETA - TRANSPORTE URBANO")
        print("Apps A vs B - Inferência Estatística")
        print("="*80)
        
        # 1. Estatísticas descritivas
        stats_a, stats_b = self.estatisticas_descritivas()
        self._imprimir_estatisticas_descritivas(stats_a, stats_b)
        
        # 2. Intervalos de confiança para médias
        self._imprimir_ic_medias()
        
        # 3. Diferença de médias
        self._imprimir_diferenca_medias()
        
        # 4. Variâncias
        self._imprimir_variancias()
        
        # 5. Razão de variâncias
        self._imprimir_razao_variancias()
        
        # 6. Proporções de aprovação
        self._imprimir_proporcoes()
        
        # 7. Diferença de proporções
        self._imprimir_diferenca_proporcoes()
        
        # 8. Análise de SLA
        self._imprimir_analise_sla()
        
        # Gerar visualizações
        self.gerar_visualizacoes()
        
        return stats_a, stats_b
    
    def _imprimir_estatisticas_descritivas(self, stats_a: dict, stats_b: dict) -> None:
        """Imprime estatísticas descritivas formatadas."""
        print("\n1. ESTATÍSTICAS DESCRITIVAS")
        print("-" * 50)
        print(f"{'Métrica':<15} {'App A':<12} {'App B':<12}")
        print("-" * 50)
        
        metricas = [
            ('N', 'n', ''),
            ('Média', 'media', '.3f'),
            ('Mediana', 'mediana', '.3f'),
            ('Desvio Padrão', 'dp', '.3f'),
            ('Variância', 'variancia', '.3f'),
            ('CV (%)', 'cv', '.1%'),
            ('P90', 'p90', '.3f'),
            ('P95', 'p95', '.3f'),
            ('IQR', 'iqr', '.3f')
        ]
        
        for nome, chave, fmt in metricas:
            if fmt == '.1%':
                val_a = f"{stats_a[chave]*100:.1f}"
                val_b = f"{stats_b[chave]*100:.1f}"
            elif fmt:
                val_a = f"{stats_a[chave]:{fmt}}"
                val_b = f"{stats_b[chave]:{fmt}}"
            else:
                val_a = str(stats_a[chave])
                val_b = str(stats_b[chave])
            
            print(f"{nome:<15} {val_a:<12} {val_b:<12}")
    
    def _imprimir_ic_medias(self) -> None:
        """Imprime intervalos de confiança para médias."""
        print("\n\n2. INTERVALOS DE CONFIANÇA PARA MÉDIAS")
        print("-" * 80)
        niveis = [0.90, 0.95, 0.99]
        
        for app, dados in [('A', self.app_a), ('B', self.app_b)]:
            print(f"\nApp {app}:")
            print(f"{'Nível':<8} {'Média':<8} {'ME':<8} {'Amplitude':<10} {'LI':<8} {'LS':<8}")
            print("-" * 50)
            for nivel in niveis:
                ic = self.ic_media(dados, nivel)
                print(f"{nivel*100:>5.0f}%   {ic['media']:>6.3f}   {ic['margem_erro']:>6.3f}   "
                      f"{ic['amplitude']:>8.3f}   {ic['li']:>6.3f}   {ic['ls']:>6.3f}")
    
    def _imprimir_diferenca_medias(self) -> None:
        """Imprime análise de diferença de médias."""
        print("\n\n3. DIFERENÇA DE MÉDIAS (A - B) - TESTE DE WELCH")
        print("-" * 80)
        print(f"{'Nível':<8} {'Diferença':<10} {'ME':<8} {'Amplitude':<10} {'LI':<8} {'LS':<8} {'Significativo':<12}")
        print("-" * 80)
        
        niveis = [0.90, 0.95, 0.99]
        for nivel in niveis:
            ic_diff = self.ic_diferenca_medias_welch(self.app_a, self.app_b, nivel)
            significativo = "Não" if ic_diff['li'] <= 0 <= ic_diff['ls'] else "Sim"
            print(f"{nivel*100:>5.0f}%   {ic_diff['diferenca']:>8.3f}   {ic_diff['margem_erro']:>6.3f}   "
                  f"{ic_diff['amplitude']:>8.3f}   {ic_diff['li']:>6.3f}   {ic_diff['ls']:>6.3f}   {significativo:<12}")
    
    def _imprimir_variancias(self) -> None:
        """Imprime intervalos de confiança para variâncias."""
        print("\n\n4. INTERVALOS DE CONFIANÇA PARA VARIÂNCIAS (95%)")
        print("-" * 60)
        print(f"{'App':<5} {'Variância':<12} {'LI':<10} {'LS':<10}")
        print("-" * 60)
        
        for app, dados in [('A', self.app_a), ('B', self.app_b)]:
            ic_var = self.ic_variancia(dados, 0.95)
            print(f"{app:<5} {ic_var['variancia']:>10.3f}   {ic_var['li']:>8.3f}   {ic_var['ls']:>8.3f}")
    
    def _imprimir_razao_variancias(self) -> None:
        """Imprime análise de razão de variâncias."""
        print("\n\n5. RAZÃO DE VARIÂNCIAS (A/B)")
        print("-" * 70)
        print(f"{'Nível':<8} {'Razão':<8} {'LI':<8} {'LS':<8} {'Iguais':<12}")
        print("-" * 70)
        
        niveis = [0.90, 0.95, 0.99]
        for nivel in niveis:
            ic_razao = self.ic_razao_variancias(self.app_a, self.app_b, nivel)
            iguais = "Sim" if ic_razao['li'] <= 1 <= ic_razao['ls'] else "Não"
            print(f"{nivel*100:>5.0f}%   {ic_razao['razao']:>6.3f}   {ic_razao['li']:>6.3f}   "
                  f"{ic_razao['ls']:>6.3f}   {iguais:<12}")
    
    def _imprimir_proporcoes(self) -> None:
        """Imprime intervalos de confiança para proporções."""
        print("\n\n6. PROPORÇÕES DE APROVAÇÃO (PESQUISA DE OPINIÃO)")
        print("-" * 80)
        
        niveis = [0.90, 0.95, 0.99]
        for app in ['A', 'B']:
            x = self.pesquisa[app]['aprovacoes']
            n = self.pesquisa[app]['total']
            print(f"\nApp {app} ({x}/{n} = {x/n:.3f}):")
            print(f"{'Nível':<8} {'Proporção':<10} {'ME':<8} {'Amplitude':<10} {'LI':<8} {'LS':<8}")
            print("-" * 60)
            
            for nivel in niveis:
                ic_prop = self.ic_proporcao_wald(x, n, nivel)
                print(f"{nivel*100:>5.0f}%   {ic_prop['proporcao']:>8.3f}   {ic_prop['margem_erro']:>6.3f}   "
                      f"{ic_prop['amplitude']:>8.3f}   {ic_prop['li']:>6.3f}   {ic_prop['ls']:>6.3f}")
    
    def _imprimir_diferenca_proporcoes(self) -> None:
        """Imprime análise de diferença de proporções."""
        print("\n\n7. DIFERENÇA DE PROPORÇÕES (A - B)")
        print("-" * 80)
        print(f"{'Nível':<8} {'Diferença':<10} {'ME':<8} {'Amplitude':<10} {'LI':<8} {'LS':<8} {'Significativo':<12}")
        print("-" * 80)
        
        x1, n1 = self.pesquisa['A']['aprovacoes'], self.pesquisa['A']['total']
        x2, n2 = self.pesquisa['B']['aprovacoes'], self.pesquisa['B']['total']
        
        niveis = [0.90, 0.95, 0.99]
        for nivel in niveis:
            ic_diff_prop = self.ic_diferenca_proporcoes_wald(x1, n1, x2, n2, nivel)
            significativo = "Não" if ic_diff_prop['li'] <= 0 <= ic_diff_prop['ls'] else "Sim"
            print(f"{nivel*100:>5.0f}%   {ic_diff_prop['diferenca']:>8.3f}   {ic_diff_prop['margem_erro']:>6.3f}   "
                  f"{ic_diff_prop['amplitude']:>8.3f}   {ic_diff_prop['li']:>6.3f}   {ic_diff_prop['ls']:>6.3f}   {significativo:<12}")
    
    def _imprimir_analise_sla(self) -> None:
        """Imprime análise de SLA."""
        print("\n\n8. ANÁLISE DE SLA (SERVICE LEVEL AGREEMENT)")
        print("-" * 60)
        limites_sla = [5, 8, 10]
        print(f"{'Limite (min)':<12} {'App A (%)':<12} {'App B (%)':<12} {'Diferença':<12}")
        print("-" * 60)
        
        for limite in limites_sla:
            sla_a = self.calcular_sla(self.app_a, limite) * 100
            sla_b = self.calcular_sla(self.app_b, limite) * 100
            diff_sla = sla_a - sla_b
            print(f"{limite:<12} {sla_a:>10.1f}   {sla_b:>10.1f}   {diff_sla:>+10.1f}")


def main():
    """Função principal para execução da análise."""
    # Configurar caminhos
    dados_path = "data/transp_dados.csv"
    output_dir = "outputs"
    
    # Verificar se arquivo existe
    if not os.path.exists(dados_path):
        print(f"Erro: Arquivo {dados_path} não encontrado!")
        print("Certifique-se de que o arquivo está no diretório 'data/'")
        return
    
    try:
        # Executar análise
        analise = AnaliseTransporte(dados_path, output_dir)
        stats_a, stats_b = analise.executar_analise_completa()
        
        print("\n" + "="*80)
        print("ANÁLISE CONCLUÍDA COM SUCESSO!")
        print("="*80)
        print(f"Resultados salvos em: {output_dir}/")
        
    except Exception as e:
        print(f"Erro durante a análise: {e}")
        raise


if __name__ == "__main__":
    main()
