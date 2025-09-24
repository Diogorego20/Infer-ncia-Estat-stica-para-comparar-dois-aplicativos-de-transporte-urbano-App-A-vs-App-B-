#!/usr/bin/env python3
"""
Testes de Hipóteses Estatísticas - Transporte Urbano

Este módulo implementa testes de hipóteses complementares à análise de
intervalos de confiança, incluindo testes de normalidade, homogeneidade
de variâncias e comparações entre grupos.

Autor: Diogo Da Silva Rego
Disciplina: Inferência Estatística I - UFPB CCEN
Matrícula: 20240045381
Data: 23/09/2025
"""

import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import (normaltest, shapiro, levene, mannwhitneyu, 
                        chi2_contingency, ttest_ind)
import warnings
from pathlib import Path

warnings.filterwarnings('ignore')


class TestesHipoteses:
    """
    Classe para execução de testes de hipóteses estatísticas.
    
    Esta classe implementa diversos testes estatísticos para validar
    pressupostos e comparar grupos de dados de aplicativos de transporte.
    
    Attributes:
        dados (pd.DataFrame): DataFrame com os dados de tempo de espera
        app_a (np.array): Dados do aplicativo A
        app_b (np.array): Dados do aplicativo B
        pesquisa (dict): Dados da pesquisa de satisfação
    """
    
    def __init__(self, dados_path: str):
        """
        Inicializa os testes com os dados de transporte.
        
        Args:
            dados_path (str): Caminho para o arquivo CSV com os dados
        """
        self.dados = pd.read_csv(dados_path)
        self.dados.columns = ['app', 'espera_min']
        
        self.app_a = self.dados[self.dados['app'] == 'A']['espera_min'].values
        self.app_b = self.dados[self.dados['app'] == 'B']['espera_min'].values
        
        # Dados da pesquisa de satisfação
        self.pesquisa = {
            'A': {'aprovacoes': 132, 'total': 150},
            'B': {'aprovacoes': 120, 'total': 150}
        }
    
    def teste_normalidade(self) -> dict:
        """
        Testa normalidade dos dados usando Shapiro-Wilk e D'Agostino.
        
        Returns:
            dict: Resultados dos testes de normalidade
        """
        print("TESTES DE NORMALIDADE")
        print("-" * 60)
        
        # Shapiro-Wilk (recomendado para n < 50)
        stat_a_sw, p_a_sw = shapiro(self.app_a)
        stat_b_sw, p_b_sw = shapiro(self.app_b)
        
        # D'Agostino-Pearson (recomendado para n >= 20)
        stat_a_da, p_a_da = normaltest(self.app_a)
        stat_b_da, p_b_da = normaltest(self.app_b)
        
        print(f"{'Teste':<20} {'App A':<15} {'App B':<15}")
        print("-" * 60)
        print(f"{'Shapiro-Wilk':<20}")
        print(f"  Estatística      {stat_a_sw:>12.4f}   {stat_b_sw:>12.4f}")
        print(f"  p-valor          {p_a_sw:>12.4f}   {p_b_sw:>12.4f}")
        print(f"  Normal (α=0.05)  {'Sim' if p_a_sw > 0.05 else 'Não':>12}   {'Sim' if p_b_sw > 0.05 else 'Não':>12}")
        
        dagostino_name = "D'Agostino-Pearson"
        print(f"\n{dagostino_name:<20}")
        print(f"  Estatística      {stat_a_da:>12.4f}   {stat_b_da:>12.4f}")
        print(f"  p-valor          {p_a_da:>12.4f}   {p_b_da:>12.4f}")
        print(f"  Normal (α=0.05)  {'Sim' if p_a_da > 0.05 else 'Não':>12}   {'Sim' if p_b_da > 0.05 else 'Não':>12}")
        
        return {
            'shapiro': {'A': (stat_a_sw, p_a_sw), 'B': (stat_b_sw, p_b_sw)},
            'dagostino': {'A': (stat_a_da, p_a_da), 'B': (stat_b_da, p_b_da)}
        }
    
    def teste_homogeneidade_variancias(self) -> tuple:
        """
        Testa homogeneidade de variâncias usando teste de Levene.
        
        Returns:
            tuple: (estatística, p-valor) do teste de Levene
        """
        print("\n\nTESTE DE HOMOGENEIDADE DE VARIÂNCIAS (LEVENE)")
        print("-" * 60)
        
        stat, p_valor = levene(self.app_a, self.app_b)
        
        print(f"Estatística de Levene: {stat:.4f}")
        print(f"p-valor: {p_valor:.4f}")
        print(f"Variâncias iguais (α=0.05): {'Sim' if p_valor > 0.05 else 'Não'}")
        
        if p_valor > 0.05:
            print("→ Recomendação: Usar teste t de Student (variâncias iguais)")
        else:
            print("→ Recomendação: Usar teste de Welch (variâncias diferentes)")
        
        return stat, p_valor
    
    def teste_diferenca_medias(self) -> dict:
        """
        Testa diferença de médias usando múltiplos métodos.
        
        Returns:
            dict: Resultados dos testes de diferença de médias
        """
        print("\n\nTESTE DE DIFERENÇA DE MÉDIAS")
        print("-" * 60)
        
        # Teste t de Welch (não assume variâncias iguais)
        stat_welch, p_welch = ttest_ind(self.app_a, self.app_b, equal_var=False)
        
        # Teste t de Student (assume variâncias iguais)
        stat_student, p_student = ttest_ind(self.app_a, self.app_b, equal_var=True)
        
        # Mann-Whitney U (não paramétrico)
        stat_mw, p_mw = mannwhitneyu(self.app_a, self.app_b, alternative='two-sided')
        
        print(f"{'Teste':<20} {'Estatística':<12} {'p-valor':<12} {'Significativo':<12}")
        print("-" * 60)
        print(f"{'Welch t-test':<20} {stat_welch:>10.4f}   {p_welch:>10.4f}   {'Sim' if p_welch < 0.05 else 'Não':>10}")
        print(f"{'Student t-test':<20} {stat_student:>10.4f}   {p_student:>10.4f}   {'Sim' if p_student < 0.05 else 'Não':>10}")
        print(f"{'Mann-Whitney U':<20} {stat_mw:>10.0f}   {p_mw:>10.4f}   {'Sim' if p_mw < 0.05 else 'Não':>10}")
        
        # Interpretação
        print(f"\nInterpretação:")
        if p_welch < 0.05:
            diff_media = np.mean(self.app_a) - np.mean(self.app_b)
            print(f"• Há evidência significativa de diferença entre as médias (p = {p_welch:.4f})")
            print(f"• App A tem tempo médio {diff_media:+.3f} min em relação ao App B")
        else:
            print(f"• Não há evidência significativa de diferença entre as médias (p = {p_welch:.4f})")
        
        return {
            'welch': (stat_welch, p_welch),
            'student': (stat_student, p_student),
            'mannwhitney': (stat_mw, p_mw)
        }
    
    def teste_diferenca_variancias(self) -> tuple:
        """
        Testa diferença de variâncias usando teste F.
        
        Returns:
            tuple: (estatística F, p-valor)
        """
        print("\n\nTESTE F PARA RAZÃO DE VARIÂNCIAS")
        print("-" * 60)
        
        var_a = np.var(self.app_a, ddof=1)
        var_b = np.var(self.app_b, ddof=1)
        
        # F-statistic (sempre colocar maior variância no numerador)
        if var_a > var_b:
            f_stat = var_a / var_b
            df1, df2 = len(self.app_a) - 1, len(self.app_b) - 1
            maior_var = "A"
        else:
            f_stat = var_b / var_a
            df1, df2 = len(self.app_b) - 1, len(self.app_a) - 1
            maior_var = "B"
        
        # p-valor bilateral
        p_valor = 2 * (1 - stats.f.cdf(f_stat, df1, df2))
        
        print(f"Variância App A: {var_a:.4f}")
        print(f"Variância App B: {var_b:.4f}")
        print(f"Razão F: {f_stat:.4f}")
        print(f"Graus de liberdade: ({df1}, {df2})")
        print(f"p-valor: {p_valor:.4f}")
        print(f"Variâncias iguais (α=0.05): {'Sim' if p_valor > 0.05 else 'Não'}")
        print(f"App com maior variabilidade: {maior_var}")
        
        return f_stat, p_valor
    
    def teste_diferenca_proporcoes(self) -> dict:
        """
        Testa diferença de proporções usando teste Z e qui-quadrado.
        
        Returns:
            dict: Resultados dos testes de proporções
        """
        print("\n\nTESTE Z PARA DIFERENÇA DE PROPORÇÕES")
        print("-" * 60)
        
        x1, n1 = self.pesquisa['A']['aprovacoes'], self.pesquisa['A']['total']
        x2, n2 = self.pesquisa['B']['aprovacoes'], self.pesquisa['B']['total']
        
        p1, p2 = x1/n1, x2/n2
        p_pool = (x1 + x2) / (n1 + n2)
        
        # Estatística Z para diferença de proporções
        se_pool = np.sqrt(p_pool * (1 - p_pool) * (1/n1 + 1/n2))
        z_stat = (p1 - p2) / se_pool
        
        # p-valor bilateral
        p_valor = 2 * (1 - stats.norm.cdf(abs(z_stat)))
        
        print(f"Proporção App A: {p1:.3f} ({x1}/{n1})")
        print(f"Proporção App B: {p2:.3f} ({x2}/{n2})")
        print(f"Diferença (A-B): {p1-p2:+.3f}")
        print(f"Proporção pooled: {p_pool:.3f}")
        print(f"Estatística Z: {z_stat:.4f}")
        print(f"p-valor: {p_valor:.4f}")
        print(f"Diferença significativa (α=0.05): {'Sim' if p_valor < 0.05 else 'Não'}")
        
        # Teste qui-quadrado de independência
        tabela = np.array([[x1, n1-x1], [x2, n2-x2]])
        chi2_stat, p_chi2, dof, expected = chi2_contingency(tabela)
        
        print(f"\nTeste Qui-quadrado de independência:")
        print(f"Estatística χ²: {chi2_stat:.4f}")
        print(f"p-valor: {p_chi2:.4f}")
        print(f"Associação significativa: {'Sim' if p_chi2 < 0.05 else 'Não'}")
        
        return {
            'z_test': (z_stat, p_valor),
            'chi2_test': (chi2_stat, p_chi2)
        }
    
    def poder_estatistico(self) -> tuple:
        """
        Calcula tamanho de efeito (Cohen's d e Cohen's h).
        
        Returns:
            tuple: (Cohen's d, Cohen's h)
        """
        print("\n\nANÁLISE DE TAMANHO DE EFEITO")
        print("-" * 60)
        
        # Cohen's d para diferença de médias
        mean_diff = np.mean(self.app_a) - np.mean(self.app_b)
        pooled_std = np.sqrt(((len(self.app_a)-1)*np.var(self.app_a, ddof=1) + 
                             (len(self.app_b)-1)*np.var(self.app_b, ddof=1)) / 
                            (len(self.app_a) + len(self.app_b) - 2))
        cohens_d = mean_diff / pooled_std
        
        # Interpretação do tamanho de efeito para Cohen's d
        if abs(cohens_d) < 0.2:
            efeito_d = "Pequeno"
        elif abs(cohens_d) < 0.5:
            efeito_d = "Pequeno a Médio"
        elif abs(cohens_d) < 0.8:
            efeito_d = "Médio a Grande"
        else:
            efeito_d = "Grande"
        
        print(f"Cohen's d (diferença de médias): {cohens_d:.3f}")
        print(f"Tamanho do efeito: {efeito_d}")
        
        # Cohen's h para diferença de proporções
        p1 = self.pesquisa['A']['aprovacoes'] / self.pesquisa['A']['total']
        p2 = self.pesquisa['B']['aprovacoes'] / self.pesquisa['B']['total']
        
        cohens_h = 2 * (np.arcsin(np.sqrt(p1)) - np.arcsin(np.sqrt(p2)))
        
        # Interpretação do tamanho de efeito para Cohen's h
        if abs(cohens_h) < 0.2:
            efeito_h = "Pequeno"
        elif abs(cohens_h) < 0.5:
            efeito_h = "Pequeno a Médio"
        elif abs(cohens_h) < 0.8:
            efeito_h = "Médio a Grande"
        else:
            efeito_h = "Grande"
        
        print(f"\nCohen's h (diferença de proporções): {cohens_h:.3f}")
        print(f"Tamanho do efeito: {efeito_h}")
        
        return cohens_d, cohens_h
    
    def executar_todos_testes(self) -> dict:
        """
        Executa todos os testes de hipóteses e retorna resumo.
        
        Returns:
            dict: Dicionário com todos os resultados dos testes
        """
        print("="*80)
        print("TESTES DE HIPÓTESES ESTATÍSTICAS - TRANSPORTE URBANO")
        print("="*80)
        
        # Executar todos os testes
        norm_results = self.teste_normalidade()
        levene_results = self.teste_homogeneidade_variancias()
        media_results = self.teste_diferenca_medias()
        var_results = self.teste_diferenca_variancias()
        prop_results = self.teste_diferenca_proporcoes()
        poder_results = self.poder_estatistico()
        
        # Resumo das conclusões
        self._imprimir_resumo_conclusoes(norm_results, levene_results, 
                                       media_results, var_results, prop_results)
        
        return {
            'normalidade': norm_results,
            'levene': levene_results,
            'medias': media_results,
            'variancias': var_results,
            'proporcoes': prop_results,
            'poder': poder_results
        }
    
    def _imprimir_resumo_conclusoes(self, norm_results: dict, levene_results: tuple,
                                  media_results: dict, var_results: tuple, 
                                  prop_results: dict) -> None:
        """Imprime resumo das conclusões dos testes."""
        print("\n\n" + "="*80)
        print("RESUMO DAS CONCLUSÕES DOS TESTES")
        print("="*80)
        
        print("\n1. NORMALIDADE DOS DADOS:")
        if (norm_results['shapiro']['A'][1] > 0.05 and 
            norm_results['shapiro']['B'][1] > 0.05):
            print("   ✓ Ambos os grupos seguem distribuição normal")
            print("   → Recomendação: Usar testes paramétricos")
        else:
            print("   ✗ Pelo menos um grupo não segue distribuição normal")
            print("   → Recomendação: Considerar testes não paramétricos")
        
        print("\n2. HOMOGENEIDADE DE VARIÂNCIAS:")
        if levene_results[1] > 0.05:
            print("   ✓ Variâncias homogêneas entre grupos")
            print("   → Recomendação: Usar teste t de Student")
        else:
            print("   ✗ Variâncias heterogêneas entre grupos")
            print("   → Recomendação: Usar teste de Welch")
        
        print("\n3. DIFERENÇA DE MÉDIAS:")
        if media_results['welch'][1] < 0.05:
            diff_media = np.mean(self.app_a) - np.mean(self.app_b)
            print("   ✓ Diferença significativa entre médias (p < 0.05)")
            print(f"   → App A tem tempo médio {diff_media:+.2f} min em relação ao App B")
        else:
            print("   ✗ Não há diferença significativa entre médias (p ≥ 0.05)")
        
        print("\n4. DIFERENÇA DE VARIÂNCIAS:")
        if var_results[1] < 0.05:
            var_a = np.var(self.app_a, ddof=1)
            var_b = np.var(self.app_b, ddof=1)
            print("   ✓ Diferença significativa entre variâncias (p < 0.05)")
            if var_a > var_b:
                print("   → App A é mais variável que App B")
            else:
                print("   → App B é mais variável que App A")
        else:
            print("   ✗ Não há diferença significativa entre variâncias (p ≥ 0.05)")
        
        print("\n5. DIFERENÇA DE PROPORÇÕES:")
        if prop_results['z_test'][1] < 0.05:
            p1 = self.pesquisa['A']['aprovacoes'] / self.pesquisa['A']['total']
            p2 = self.pesquisa['B']['aprovacoes'] / self.pesquisa['B']['total']
            print("   ✓ Diferença significativa entre proporções (p < 0.05)")
            print(f"   → App A tem {(p1-p2)*100:+.1f} pontos percentuais a mais de aprovação")
        else:
            print("   ✗ Não há diferença significativa entre proporções (p ≥ 0.05)")


def main():
    """Função principal para execução dos testes."""
    dados_path = "data/transp_dados.csv"
    
    # Verificar se arquivo existe
    if not Path(dados_path).exists():
        print(f"Erro: Arquivo {dados_path} não encontrado!")
        print("Certifique-se de que o arquivo está no diretório 'data/'")
        return
    
    try:
        # Executar testes
        testes = TestesHipoteses(dados_path)
        resultados = testes.executar_todos_testes()
        
        print("\n" + "="*80)
        print("TESTES DE HIPÓTESES CONCLUÍDOS!")
        print("="*80)
        
    except Exception as e:
        print(f"Erro durante os testes: {e}")
        raise


if __name__ == "__main__":
    main()
