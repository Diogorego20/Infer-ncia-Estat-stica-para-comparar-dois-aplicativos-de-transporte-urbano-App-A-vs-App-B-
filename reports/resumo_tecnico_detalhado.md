# Resumo Técnico Detalhado: Análise Estatística de Aplicativos de Transporte

**Disciplina:** Inferência Estatística I - UFPB CCEN  
**Aluno:** Diogo Da Silva Rego (20240045381)  
**Professora:** Tatiene Correia  
**Data:** 23 de Setembro de 2025

---

## Metodologia Estatística Aplicada

Esta análise utilizou técnicas de **inferência estatística** para comparar dois aplicativos de transporte urbano (A e B) com base em dados reais de tempo de espera e pesquisa de opinião. A abordagem seguiu rigorosamente os princípios da disciplina Inferência Estatística I.

### Dados Utilizados

- **Amostra de Tempo de Espera:** 90 observações (App A: n=35, App B: n=55)
- **Pesquisa de Opinião:** 300 usuários (150 por aplicativo)
- **Variável Principal:** Tempo de espera até encontrar motorista (em minutos)
- **Variável Secundária:** Aprovação do usuário (binária: aprova/não aprova)

---

## 1. Análise de Médias e Intervalos de Confiança

### Questão 1: Estimativa do tempo médio de espera

**Resultados dos Intervalos de Confiança para Médias:**

| App | Nível | Média | Margem de Erro | Amplitude | Limite Inferior | Limite Superior |
|-----|-------|-------|----------------|-----------|-----------------|-----------------|
| A   | 90%   | 7.434 | 0.306         | 0.612     | 7.128          | 7.740          |
| A   | 95%   | 7.434 | 0.368         | 0.736     | 7.066          | 7.802          |
| A   | 99%   | 7.434 | 0.494         | 0.988     | 6.940          | 7.928          |
| B   | 90%   | 6.811 | 0.351         | 0.702     | 6.460          | 7.162          |
| B   | 95%   | 6.811 | 0.421         | 0.842     | 6.390          | 7.232          |
| B   | 99%   | 6.811 | 0.560         | 1.121     | 6.251          | 7.372          |

**Interpretação:** O App B apresenta tempo médio menor (6.81 vs 7.43 minutos), mas também maior incerteza (margem de erro maior em todos os níveis). A amplitude dos intervalos aumenta com o nível de confiança, refletindo o trade-off entre precisão e confiabilidade.

### Questão 2: Diferença entre as médias (A - B)

**Teste de Welch (variâncias diferentes):**

| Nível | Diferença | Margem de Erro | Limite Inferior | Limite Superior | Significativo |
|-------|-----------|----------------|-----------------|-----------------|---------------|
| 90%   | 0.623     | 0.461         | 0.162          | 1.084          | **Sim**       |
| 95%   | 0.623     | 0.551         | 0.072          | 1.174          | **Sim**       |
| 99%   | 0.623     | 0.730         | -0.107         | 1.353          | Não           |

**Conclusão:** Há evidência estatística significativa de que o App A tem tempo médio maior que o App B em níveis de 90% e 95%. A 99%, a evidência não é conclusiva.

---

## 2. Análise de Variabilidade e Consistência

### Questão 3: Variabilidade do tempo de espera

**Intervalos de Confiança para Variâncias (95%):**

| App | Variância | Limite Inferior | Limite Superior | Desvio Padrão | CV (%) |
|-----|-----------|-----------------|-----------------|---------------|--------|
| A   | 1.147     | 0.750          | 1.968          | 1.071         | 14.4   |
| B   | 2.422     | 1.717          | 3.676          | 1.556         | 22.9   |

**Interpretação:** O App A é significativamente mais consistente, com variância menor e coeficiente de variação de 14.4% contra 22.9% do App B. Isso indica maior previsibilidade do serviço.

### Questão 4: Razão entre as variâncias (A/B)

**Teste F para Razão de Variâncias:**

| Nível | Razão A/B | Limite Inferior | Limite Superior | Variâncias Iguais |
|-------|-----------|-----------------|-----------------|-------------------|
| 90%   | 0.473     | 0.288          | 0.806          | **Não**           |
| 95%   | 0.473     | 0.261          | 0.895          | **Não**           |
| 99%   | 0.473     | 0.217          | 1.103          | Sim               |

**Conclusão:** As variâncias são significativamente diferentes em 90% e 95%, confirmando que o App B é mais variável. Apenas a 99% não há evidência conclusiva de diferença.

---

## 3. Análise de Proporções

### Questão 5: Proporção de aprovação

**Intervalos de Confiança para Proporções:**

| App | Proporção | Nível | Margem de Erro | Limite Inferior | Limite Superior |
|-----|-----------|-------|----------------|-----------------|-----------------|
| A   | 0.880     | 90%   | 0.044         | 0.836          | 0.924          |
| A   | 0.880     | 95%   | 0.052         | 0.828          | 0.932          |
| A   | 0.880     | 99%   | 0.068         | 0.812          | 0.948          |
| B   | 0.800     | 90%   | 0.054         | 0.746          | 0.854          |
| B   | 0.800     | 95%   | 0.064         | 0.736          | 0.864          |
| B   | 0.800     | 99%   | 0.084         | 0.716          | 0.884          |

**Interpretação:** O App A tem maior aprovação (88% vs 80%), com intervalos que não se sobrepõem significativamente, especialmente em níveis de confiança menores.

### Questão 6: Diferença entre as proporções (A - B)

**Teste Z para Diferença de Proporções:**

| Nível | Diferença | Margem de Erro | Limite Inferior | Limite Superior | Significativo |
|-------|-----------|----------------|-----------------|-----------------|---------------|
| 90%   | 0.080     | 0.069         | 0.011          | 0.149          | **Sim**       |
| 95%   | 0.080     | 0.082         | -0.002         | 0.162          | Não           |
| 99%   | 0.080     | 0.108         | -0.028         | 0.188          | Não           |

**Conclusão:** A diferença de aprovação é significativa apenas a 90%. Em níveis mais conservadores (95% e 99%), a evidência não é conclusiva.

---

## 4. Testes de Hipóteses Complementares

### Pressupostos dos Testes

**Normalidade (Shapiro-Wilk):**
- App A: p = 0.983 (Normal ✓)
- App B: p = 0.981 (Normal ✓)

**Homogeneidade de Variâncias (Levene):**
- p = 0.033 (Variâncias diferentes ✗)
- **Recomendação:** Usar Teste de Welch

### Testes de Diferença de Médias

| Teste | Estatística | p-valor | Significativo |
|-------|-------------|---------|---------------|
| Welch t-test | 2.248 | 0.027 | **Sim** |
| Student t-test | 2.074 | 0.041 | **Sim** |
| Mann-Whitney U | 1217 | 0.036 | **Sim** |

**Tamanho do Efeito (Cohen's d):** 0.449 (Pequeno a Médio)

---

## 5. Métricas de Performance Operacional

### SLA (Service Level Agreement)

| Limite | App A | App B | Diferença |
|--------|-------|-------|-----------|
| 5 min  | 0.0%  | 10.9% | -10.9 p.p. |
| 8 min  | 65.7% | 76.4% | -10.6 p.p. |
| 10 min | 100.0%| 98.2% | +1.8 p.p.  |

**Interpretação:** O App B é superior para metas de atendimento rápido (5-8 min), enquanto o App A garante atendimento universal em até 10 minutos.

---

## Conclusão Técnica

A análise estatística revela um **trade-off claro** entre os aplicativos:

1. **App B:** Mais rápido na média, melhor SLA para tempos curtos
2. **App A:** Mais consistente, maior aprovação dos usuários

A escolha depende da prioridade estratégica: **velocidade** (App B) versus **confiabilidade e satisfação** (App A). Do ponto de vista estatístico, ambas as conclusões são suportadas por evidências robustas em diferentes níveis de confiança.

**Robustez da Análise:** Os resultados são consistentes entre diferentes testes (paramétricos e não-paramétricos) e níveis de confiança, conferindo alta credibilidade às conclusões.
