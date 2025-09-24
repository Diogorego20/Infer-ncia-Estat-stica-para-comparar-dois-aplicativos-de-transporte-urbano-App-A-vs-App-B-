#!/usr/bin/env python3
"""
Visualizações Executivas e Métricas-Chave - Transporte Urbano

Este módulo cria visualizações profissionais e dashboards executivos
para apresentação de resultados da análise estatística de aplicativos
de transporte urbano.

Autor: Diogo Da Silva Rego
Disciplina: Inferência Estatística I - UFPB CCEN
Matrícula: 20240045381
Data: 23/09/2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import t, norm, gaussian_kde
import warnings
from pathlib import Path

warnings.filterwarnings('ignore')

# Configuração para visualizações profissionais
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.size': 12,
    'font.family': 'DejaVu Sans',
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'legend.fontsize': 11,
    'figure.titlesize': 16,
    'figure.figsize': (12, 8),
    'axes.grid': True,
    'grid.alpha': 0.3
})


class VisualizacoesExecutivas:
    """
    Classe para criação de visualizações executivas.
    
    Esta classe gera gráficos profissionais e dashboards para
    apresentação de resultados da análise estatística.
    
    Attributes:
        dados (pd.DataFrame): DataFrame com os dados de tempo de espera
        app_a (np.array): Dados do aplicativo A
        app_b (np.array): Dados do aplicativo B
        cores (dict): Paleta de cores corporativas
        pesquisa (dict): Dados da pesquisa de satisfação
    """
    
    def __init__(self, dados_path: str, output_dir: str = "outputs"):
        """
        Inicializa com os dados de transporte.
        
        Args:
            dados_path (str): Caminho para o arquivo CSV com os dados
            output_dir (str): Diretório para salvar visualizações
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        self.dados = pd.read_csv(dados_path)
        self.dados.columns = ['app', 'espera_min']
        
        self.app_a = self.dados[self.dados['app'] == 'A']['espera_min'].values
        self.app_b = self.dados[self.dados['app'] == 'B']['espera_min'].values
        
        # Paleta de cores corporativas
        self.cores = {
            'A': '#2E86AB',      # Azul profissional
            'B': '#A23B72',      # Roxo profissional
            'destaque': '#F18F01', # Laranja para destaques
            'neutro': '#C5C3C6'   # Cinza neutro
        }
        
        # Dados da pesquisa de satisfação
        self.pesquisa = {
            'A': {'aprovacoes': 132, 'total': 150},
            'B': {'aprovacoes': 120, 'total': 150}
        }
    
    def calcular_metricas_executivas(self) -> dict:
        """
        Calcula métricas-chave para o dashboard executivo.
        
        Returns:
            dict: Dicionário com todas as métricas calculadas
        """
        metricas = {}
        
        # Métricas de tempo
        metricas['tempo'] = {
            'A': {
                'media': np.mean(self.app_a),
                'mediana': np.median(self.app_a),
                'p90': np.percentile(self.app_a, 90),
                'dp': np.std(self.app_a, ddof=1),
                'cv': np.std(self.app_a, ddof=1) / np.mean(self.app_a) * 100
            },
            'B': {
                'media': np.mean(self.app_b),
                'mediana': np.median(self.app_b),
                'p90': np.percentile(self.app_b, 90),
                'dp': np.std(self.app_b, ddof=1),
                'cv': np.std(self.app_b, ddof=1) / np.mean(self.app_b) * 100
            }
        }
        
        # SLA (% atendimentos em até X minutos)
        metricas['sla'] = {}
        for limite in [5, 8, 10]:
            metricas['sla'][f'{limite}min'] = {
                'A': np.mean(self.app_a <= limite) * 100,
                'B': np.mean(self.app_b <= limite) * 100
            }
        
        # Aprovação
        metricas['aprovacao'] = {
            'A': self.pesquisa['A']['aprovacoes'] / self.pesquisa['A']['total'] * 100,
            'B': self.pesquisa['B']['aprovacoes'] / self.pesquisa['B']['total'] * 100
        }
        
        return metricas
    
    def _calcular_ic_media(self, dados: np.array, confianca: float = 0.95) -> dict:
        """Calcula IC para média."""
        n = len(dados)
        media = np.mean(dados)
        dp = np.std(dados, ddof=1)
        se = dp / np.sqrt(n)
        
        alpha = 1 - confianca
        t_crit = t.ppf(1 - alpha/2, df=n-1)
        me = t_crit * se
        
        return {'media': media, 'margem_erro': me, 'li': media - me, 'ls': media + me}
    
    def _calcular_ic_proporcao(self, x: int, n: int, confianca: float = 0.95) -> dict:
        """Calcula IC para proporção."""
        p = x / n
        alpha = 1 - confianca
        z_crit = norm.ppf(1 - alpha/2)
        se = np.sqrt(p * (1-p) / n)
        me = z_crit * se
        
        return {'proporcao': p, 'margem_erro': me, 'li': p - me, 'ls': p + me}
    
    def dashboard_executivo(self) -> None:
        """Cria dashboard executivo com métricas principais."""
        fig = plt.figure(figsize=(16, 12))
        gs = fig.add_gridspec(3, 4, hspace=0.3, wspace=0.3)
        
        metricas = self.calcular_metricas_executivas()
        
        # Título principal
        fig.suptitle('DASHBOARD EXECUTIVO - ANÁLISE COMPARATIVA DE APLICATIVOS DE TRANSPORTE\n' +
                    'Apps A vs B | Dados: 90 observações | Pesquisa: 300 usuários',
                    fontsize=18, fontweight='bold', y=0.95)
        
        # 1. Comparação de médias com IC
        ax1 = fig.add_subplot(gs[0, :2])
        self._grafico_comparacao_medias(ax1, metricas)
        
        # 2. Distribuições sobrepostas
        ax2 = fig.add_subplot(gs[0, 2:])
        self._grafico_distribuicoes(ax2)
        
        # 3. Métricas de SLA
        ax3 = fig.add_subplot(gs[1, :2])
        self._grafico_sla(ax3, metricas)
        
        # 4. Aprovação dos usuários
        ax4 = fig.add_subplot(gs[1, 2:])
        self._grafico_aprovacao(ax4, metricas)
        
        # 5. Resumo de KPIs
        ax5 = fig.add_subplot(gs[2, :])
        self._tabela_kpis(ax5, metricas)
        
        output_path = self.output_dir / 'dashboard_executivo.png'
        plt.savefig(output_path, dpi=300, bbox_inches='tight',
                   facecolor='white', edgecolor='none')
        plt.close()
        
        print(f"Dashboard executivo salvo em: {output_path}")
    
    def _grafico_comparacao_medias(self, ax, metricas: dict) -> None:
        """Gráfico de comparação de médias com intervalos de confiança."""
        apps = ['App A', 'App B']
        medias = [metricas['tempo']['A']['media'], metricas['tempo']['B']['media']]
        
        # Calcular ICs 95%
        ic_a = self._calcular_ic_media(self.app_a, 0.95)
        ic_b = self._calcular_ic_media(self.app_b, 0.95)
        
        erros = [ic_a['margem_erro'], ic_b['margem_erro']]
        cores = [self.cores['A'], self.cores['B']]
        
        bars = ax.bar(apps, medias, yerr=erros, capsize=8, color=cores, alpha=0.8,
                     edgecolor='black', linewidth=1)
        
        # Adicionar valores nas barras
        for i, (bar, media, erro) in enumerate(zip(bars, medias, erros)):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + erro + 0.1,
                   f'{media:.2f}±{erro:.2f}', ha='center', va='bottom', fontweight='bold')
        
        ax.set_title('Tempo Médio de Espera (IC 95%)', fontweight='bold')
        ax.set_ylabel('Tempo (minutos)')
        ax.set_ylim(0, max(medias) + max(erros) + 1)
        
        # Adicionar linha de diferença
        diff = medias[0] - medias[1]
        ax.text(0.5, max(medias) + max(erros) + 0.5, 
               f'Diferença: {diff:+.2f} min\n(App A - App B)',
               ha='center', va='center', fontsize=11, 
               bbox=dict(boxstyle="round,pad=0.3", facecolor=self.cores['destaque'], alpha=0.7))
    
    def _grafico_distribuicoes(self, ax) -> None:
        """Gráfico de distribuições sobrepostas."""
        # Histogramas
        ax.hist(self.app_a, bins=15, alpha=0.6, color=self.cores['A'], 
               label='App A', density=True, edgecolor='black', linewidth=0.5)
        ax.hist(self.app_b, bins=15, alpha=0.6, color=self.cores['B'], 
               label='App B', density=True, edgecolor='black', linewidth=0.5)
        
        # Curvas de densidade
        x_range = np.linspace(min(min(self.app_a), min(self.app_b)), 
                             max(max(self.app_a), max(self.app_b)), 100)
        
        kde_a = gaussian_kde(self.app_a)
        kde_b = gaussian_kde(self.app_b)
        
        ax.plot(x_range, kde_a(x_range), color=self.cores['A'], linewidth=3, alpha=0.8)
        ax.plot(x_range, kde_b(x_range), color=self.cores['B'], linewidth=3, alpha=0.8)
        
        # Linhas das médias
        ax.axvline(np.mean(self.app_a), color=self.cores['A'], linestyle='--', 
                  linewidth=2, alpha=0.8, label=f'Média A: {np.mean(self.app_a):.2f}')
        ax.axvline(np.mean(self.app_b), color=self.cores['B'], linestyle='--', 
                  linewidth=2, alpha=0.8, label=f'Média B: {np.mean(self.app_b):.2f}')
        
        ax.set_title('Distribuição dos Tempos de Espera', fontweight='bold')
        ax.set_xlabel('Tempo (minutos)')
        ax.set_ylabel('Densidade')
        ax.legend()
    
    def _grafico_sla(self, ax, metricas: dict) -> None:
        """Gráfico de SLA (Service Level Agreement)."""
        limites = ['5 min', '8 min', '10 min']
        sla_a = [metricas['sla']['5min']['A'], metricas['sla']['8min']['A'], metricas['sla']['10min']['A']]
        sla_b = [metricas['sla']['5min']['B'], metricas['sla']['8min']['B'], metricas['sla']['10min']['B']]
        
        x = np.arange(len(limites))
        width = 0.35
        
        bars1 = ax.bar(x - width/2, sla_a, width, label='App A', color=self.cores['A'], alpha=0.8)
        bars2 = ax.bar(x + width/2, sla_b, width, label='App B', color=self.cores['B'], alpha=0.8)
        
        # Adicionar valores nas barras
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                       f'{height:.1f}%', ha='center', va='bottom', fontweight='bold')
        
        ax.set_title('SLA - Atendimentos Dentro do Prazo', fontweight='bold')
        ax.set_ylabel('Percentual de Atendimentos (%)')
        ax.set_xlabel('Limite de Tempo')
        ax.set_xticks(x)
        ax.set_xticklabels(limites)
        ax.legend()
        ax.set_ylim(0, 110)
    
    def _grafico_aprovacao(self, ax, metricas: dict) -> None:
        """Gráfico de aprovação dos usuários."""
        apps = ['App A', 'App B']
        aprovacao = [metricas['aprovacao']['A'], metricas['aprovacao']['B']]
        
        # Calcular ICs para proporções
        ic_a = self._calcular_ic_proporcao(132, 150, 0.95)
        ic_b = self._calcular_ic_proporcao(120, 150, 0.95)
        
        erros = [ic_a['margem_erro'] * 100, ic_b['margem_erro'] * 100]
        cores = [self.cores['A'], self.cores['B']]
        
        bars = ax.bar(apps, aprovacao, yerr=erros, capsize=8, color=cores, alpha=0.8,
                     edgecolor='black', linewidth=1)
        
        # Adicionar valores nas barras
        for i, (bar, aprov, erro) in enumerate(zip(bars, aprovacao, erros)):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + erro + 1,
                   f'{aprov:.1f}%±{erro:.1f}%', ha='center', va='bottom', fontweight='bold')
        
        ax.set_title('Aprovação dos Usuários (IC 95%)', fontweight='bold')
        ax.set_ylabel('Percentual de Aprovação (%)')
        ax.set_ylim(0, 100)
        
        # Adicionar diferença
        diff = aprovacao[0] - aprovacao[1]
        ax.text(0.5, 95, f'Diferença: {diff:+.1f} p.p.',
               ha='center', va='center', fontsize=11,
               bbox=dict(boxstyle="round,pad=0.3", facecolor=self.cores['destaque'], alpha=0.7))
    
    def _tabela_kpis(self, ax, metricas: dict) -> None:
        """Tabela resumo com KPIs principais."""
        ax.axis('off')
        
        # Dados para a tabela
        kpis = [
            ['Métrica', 'App A', 'App B', 'Melhor', 'Diferença'],
            ['Tempo Médio (min)', f"{metricas['tempo']['A']['media']:.2f}", 
             f"{metricas['tempo']['B']['media']:.2f}", 'App B', 
             f"{metricas['tempo']['A']['media'] - metricas['tempo']['B']['media']:+.2f}"],
            ['Mediana (min)', f"{metricas['tempo']['A']['mediana']:.2f}", 
             f"{metricas['tempo']['B']['mediana']:.2f}", 'App B', 
             f"{metricas['tempo']['A']['mediana'] - metricas['tempo']['B']['mediana']:+.2f}"],
            ['P90 (min)', f"{metricas['tempo']['A']['p90']:.2f}", 
             f"{metricas['tempo']['B']['p90']:.2f}", 'App A', 
             f"{metricas['tempo']['A']['p90'] - metricas['tempo']['B']['p90']:+.2f}"],
            ['Coef. Variação (%)', f"{metricas['tempo']['A']['cv']:.1f}", 
             f"{metricas['tempo']['B']['cv']:.1f}", 'App A', 
             f"{metricas['tempo']['A']['cv'] - metricas['tempo']['B']['cv']:+.1f}"],
            ['SLA 8min (%)', f"{metricas['sla']['8min']['A']:.1f}", 
             f"{metricas['sla']['8min']['B']:.1f}", 'App B', 
             f"{metricas['sla']['8min']['A'] - metricas['sla']['8min']['B']:+.1f}"],
            ['Aprovação (%)', f"{metricas['aprovacao']['A']:.1f}", 
             f"{metricas['aprovacao']['B']:.1f}", 'App A', 
             f"{metricas['aprovacao']['A'] - metricas['aprovacao']['B']:+.1f}"]
        ]
        
        # Criar tabela
        table = ax.table(cellText=kpis[1:], colLabels=kpis[0], 
                        cellLoc='center', loc='center',
                        colWidths=[0.25, 0.15, 0.15, 0.15, 0.15])
        
        # Formatação da tabela
        table.auto_set_font_size(False)
        table.set_fontsize(11)
        table.scale(1, 2)
        
        # Colorir cabeçalho
        for i in range(len(kpis[0])):
            table[(0, i)].set_facecolor('#4472C4')
            table[(0, i)].set_text_props(weight='bold', color='white')
        
        # Colorir coluna "Melhor"
        for i in range(1, len(kpis)):
            if 'App A' in kpis[i][3]:
                table[(i, 3)].set_facecolor(self.cores['A'])
                table[(i, 3)].set_text_props(color='white', weight='bold')
            elif 'App B' in kpis[i][3]:
                table[(i, 3)].set_facecolor(self.cores['B'])
                table[(i, 3)].set_text_props(color='white', weight='bold')
        
        ax.set_title('RESUMO EXECUTIVO - INDICADORES-CHAVE DE PERFORMANCE (KPIs)', 
                    fontweight='bold', fontsize=14, pad=20)
    
    def grafico_boxplot_executivo(self) -> None:
        """Boxplot executivo com estatísticas."""
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Dados para boxplot
        dados_plot = [self.app_a, self.app_b]
        labels = ['App A', 'App B']
        cores = [self.cores['A'], self.cores['B']]
        
        # Criar boxplot
        bp = ax.boxplot(dados_plot, labels=labels, patch_artist=True, 
                       notch=True, showmeans=True)
        
        # Colorir boxplots
        for patch, cor in zip(bp['boxes'], cores):
            patch.set_facecolor(cor)
            patch.set_alpha(0.7)
        
        # Adicionar pontos individuais
        for i, dados in enumerate(dados_plot):
            y = dados
            x = np.random.normal(i+1, 0.04, size=len(y))
            ax.scatter(x, y, alpha=0.4, color=cores[i], s=20)
        
        # Adicionar estatísticas
        stats_text = []
        for i, (dados, label) in enumerate(zip(dados_plot, labels)):
            media = np.mean(dados)
            mediana = np.median(dados)
            q1 = np.percentile(dados, 25)
            q3 = np.percentile(dados, 75)
            
            stats_text.append(f'{label}:\nMédia: {media:.2f}\nMediana: {mediana:.2f}\nQ1: {q1:.2f}\nQ3: {q3:.2f}')
        
        # Adicionar texto com estatísticas
        ax.text(0.02, 0.98, '\n\n'.join(stats_text), transform=ax.transAxes,
               verticalalignment='top', fontsize=10,
               bbox=dict(boxstyle="round,pad=0.5", facecolor='white', alpha=0.8))
        
        ax.set_title('Distribuição dos Tempos de Espera por Aplicativo\n' +
                    'Boxplot com Pontos Individuais e Estatísticas Descritivas',
                    fontweight='bold', fontsize=14)
        ax.set_ylabel('Tempo de Espera (minutos)')
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        output_path = self.output_dir / 'boxplot_executivo.png'
        plt.savefig(output_path, dpi=300, bbox_inches='tight',
                   facecolor='white', edgecolor='none')
        plt.close()
        
        print(f"Boxplot executivo salvo em: {output_path}")
    
    def gerar_todas_visualizacoes(self) -> None:
        """Gera todas as visualizações executivas."""
        print("Gerando visualizações executivas...")
        
        # 1. Dashboard principal
        self.dashboard_executivo()
        print("✓ Dashboard executivo criado")
        
        # 2. Boxplot executivo
        self.grafico_boxplot_executivo()
        print("✓ Boxplot executivo criado")
        
        print(f"\nVisualizações salvas em: {self.output_dir}/")


def main():
    """Função principal para geração das visualizações."""
    dados_path = "data/transp_dados.csv"
    output_dir = "outputs"
    
    # Verificar se arquivo existe
    if not Path(dados_path).exists():
        print(f"Erro: Arquivo {dados_path} não encontrado!")
        print("Certifique-se de que o arquivo está no diretório 'data/'")
        return
    
    try:
        # Gerar visualizações
        viz = VisualizacoesExecutivas(dados_path, output_dir)
        viz.gerar_todas_visualizacoes()
        
        print("\n" + "="*80)
        print("VISUALIZAÇÕES EXECUTIVAS CONCLUÍDAS!")
        print("="*80)
        
    except Exception as e:
        print(f"Erro durante a geração: {e}")
        raise


if __name__ == "__main__":
    main()
