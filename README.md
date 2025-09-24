# Análise Estatística Comparativa: Aplicativos de Transporte Urbano

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Complete-success.svg)]()

## 📋 Descrição do Projeto

Análise estatística completa comparando dois aplicativos de transporte urbano (App A vs App B) para fundamentar decisões de política pública sobre contratos e incentivos. O projeto utiliza técnicas de inferência estatística para avaliar performance operacional e satisfação do usuário.

## 🎯 Objetivos

- **Comparar eficiência operacional** entre os aplicativos A e B
- **Analisar satisfação do usuário** através de pesquisa de opinião
- **Fornecer recomendações acionáveis** para gestores públicos
- **Quantificar impacto financeiro** das decisões de incentivo

## 📊 Metodologia

### Dados Analisados
- **Amostra temporal:** 90 observações de tempo de espera
  - App A: 35 observações
  - App B: 55 observações
- **Pesquisa de satisfação:** 300 usuários (150 por aplicativo)

### Técnicas Estatísticas
- Intervalos de confiança (90%, 95%, 99%)
- Teste t de Welch para diferença de médias
- Teste F para razão de variâncias
- Teste Z para diferença de proporções
- Análise de SLA (Service Level Agreement)

## 🚀 Como Executar

### Pré-requisitos
```bash
Python 3.11+
pip install -r requirements.txt
```

### Instalação
```bash
git clone https://github.com/Diogorego20/Inferencia-Estatistica-para-comparar-dois-aplicativos-de-transporte-urbano-App-A-vs-App-B-.git
cd Inferencia-Estatistica-para-comparar-dois-aplicativos-de-transporte-urbano-App-A-vs-App-B-
pip install -r requirements.txt
```

### Execução da Análise
```bash
# Análise completa
python src/analise_transporte.py

# Testes de hipóteses
python src/testes_hipoteses.py

# Visualizações executivas
python src/visualizacoes_executivas.py
```

## 📁 Estrutura do Projeto

```
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
├── data/
│   └── transp_dados.csv
├── src/
│   ├── __init__.py
│   ├── analise_transporte.py
│   ├── testes_hipoteses.py
│   └── visualizacoes_executivas.py
├── outputs/
│   ├── dashboard_executivo.png
│   ├── boxplot_executivo.png
│   ├── intervalos_confianca.png
│   └── visualizacoes_transporte.png
├── reports/
│   ├── relatorio_executivo.md
│   ├── resumo_tecnico_detalhado.md
│   └── analise_impacto_financeiro.md
└── docs/
    ├── metodologia.md
    └── interpretacao_resultados.md
```

## 📈 Principais Resultados

### Métricas-Chave

| Métrica | App A | App B | Melhor |
|---------|-------|-------|--------|
| **Tempo Médio** | 7.43 min | 6.81 min | App B |
| **Consistência (CV)** | 14.4% | 22.9% | App A |
| **Aprovação** | 88% | 80% | App A |
| **SLA 8min** | 65.7% | 76.4% | App B |

### Recomendação Principal
**App A** é recomendado como parceiro prioritário devido à:
- Maior consistência operacional (38% menos variável)
- Superior satisfação do usuário (8 p.p. de diferença)
- Menor risco financeiro (economia de R$ 2,08 milhões/ano)

## 💰 Impacto Financeiro

### Custos Adicionais do App B (Anual)
- **Atendimento ao cliente:** R$ 252.000
- **Marketing/Reputação:** R$ 336.000
- **Churn e aquisição:** R$ 504.000
- **Produtividade urbana:** R$ 990.000
- **Total:** R$ 2.082.000

### ROI da Escolha do App A
- **Investimento adicional:** R$ 50.000/mês
- **Economia total:** R$ 173.500/mês
- **ROI:** 247%
- **Payback:** 12 dias

## 📊 Visualizações

O projeto gera automaticamente:
- Dashboard executivo com KPIs principais
- Boxplots comparativos
- Gráficos de intervalos de confiança
- Análise de distribuições

## 🔬 Fundamentação Estatística

### Testes Realizados
- **Normalidade:** Shapiro-Wilk e D'Agostino
- **Homogeneidade:** Teste de Levene
- **Diferença de médias:** Welch t-test
- **Diferença de variâncias:** Teste F
- **Diferença de proporções:** Teste Z

### Níveis de Significância
- Intervalos de confiança: 90%, 95%, 99%
- Testes de hipóteses: α = 0.05
- Tamanho de efeito: Cohen's d e Cohen's h

## 📚 Documentação

- [Metodologia Detalhada](docs/metodologia.md)
- [Interpretação dos Resultados](docs/interpretacao_resultados.md)
- [Relatório Executivo](reports/relatorio_executivo.md)
- [Análise Técnica Completa](reports/resumo_tecnico_detalhado.md)

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor:
1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Diogo Da Silva Rego**
- Matrícula: 20240045381
- Disciplina: Inferência Estatística I - UFPB CCEN
- Professora: Tatiene Correia

## 📞 Contato

Para dúvidas ou sugestões, abra uma [issue](https://github.com/Diogorego20/Inferencia-Estatistica-para-comparar-dois-aplicativos-de-transporte-urbano-App-A-vs-App-B-/issues) no repositório.

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!
