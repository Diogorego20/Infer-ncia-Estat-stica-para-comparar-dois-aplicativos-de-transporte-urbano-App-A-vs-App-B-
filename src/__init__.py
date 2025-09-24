"""
Análise Estatística Comparativa: Aplicativos de Transporte Urbano

Este pacote contém módulos para análise estatística comparativa entre
aplicativos de transporte urbano, incluindo análise de tempo de espera,
testes de hipóteses e visualizações executivas.

Módulos:
    analise_transporte: Análise estatística principal
    testes_hipoteses: Testes de hipóteses complementares
    visualizacoes_executivas: Geração de gráficos e dashboards

Autor: Diogo Da Silva Rego
Disciplina: Inferência Estatística I - UFPB CCEN
"""

__version__ = "1.0.0"
__author__ = "Diogo Da Silva Rego"
__email__ = "diogo.rego@academico.ufpb.br"

from .analise_transporte import AnaliseTransporte
from .testes_hipoteses import TestesHipoteses
from .visualizacoes_executivas import VisualizacoesExecutivas

__all__ = [
    "AnaliseTransporte",
    "TestesHipoteses", 
    "VisualizacoesExecutivas"
]
