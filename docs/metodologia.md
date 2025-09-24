# Metodologia Estatística

**Projeto:** Análise Comparativa de Aplicativos de Transporte Urbano  
**Autor:** Diogo Da Silva Rego  
**Disciplina:** Inferência Estatística I - UFPB CCEN

---

## Visão Geral

Este documento detalha a metodologia estatística utilizada na análise comparativa entre os aplicativos de transporte A e B. A abordagem segue rigorosamente os princípios de inferência estatística, utilizando técnicas apropriadas para cada tipo de variável e respeitando os pressupostos dos testes.

---

## 1. Delineamento do Estudo

### Tipo de Estudo
- **Estudo observacional transversal** com análise comparativa entre dois grupos independentes

### Variáveis Analisadas

#### Variável Principal
- **Tempo de espera** (quantitativa contínua)
  - Unidade: minutos
  - Definição: Tempo decorrido entre solicitação e encontro com motorista

#### Variável Secundária
- **Aprovação do usuário** (qualitativa binária)
  - Categorias: Aprova / Não aprova
  - Fonte: Pesquisa de satisfação

#### Variável de Agrupamento
- **Aplicativo** (qualitativa nominal)
  - Categorias: A / B

---

## 2. Amostragem e Coleta de Dados

### Amostra de Tempo de Espera
- **Tamanho total:** n = 90 observações
- **App A:** n₁ = 35 observações
- **App B:** n₂ = 55 observações
- **Método:** Amostragem por conveniência em condições similares

### Pesquisa de Satisfação
- **Tamanho total:** N = 300 usuários
- **App A:** N₁ = 150 usuários (132 aprovações)
- **App B:** N₂ = 150 usuários (120 aprovações)
- **Método:** Amostragem aleatória estratificada por aplicativo

---

## 3. Análise Estatística Descritiva

### Medidas de Tendência Central
- **Média aritmética:** μ̂ = (Σxᵢ)/n
- **Mediana:** Q₂ (percentil 50)
- **Percentis:** P₉₀, P₉₅ para análise de SLA

### Medidas de Dispersão
- **Desvio padrão amostral:** s = √[Σ(xᵢ-x̄)²/(n-1)]
- **Variância amostral:** s² = Σ(xᵢ-x̄)²/(n-1)
- **Coeficiente de variação:** CV = (s/x̄) × 100%
- **Amplitude interquartílica:** IQR = Q₃ - Q₁

---

## 4. Inferência Estatística

### 4.1 Intervalos de Confiança para Médias

#### Pressupostos
- Normalidade dos dados (verificada via Shapiro-Wilk)
- Observações independentes

#### Método
**Distribuição t de Student:**
```
IC(μ; 1-α) = x̄ ± t(α/2; n-1) × (s/√n)
```

Onde:
- x̄ = média amostral
- t(α/2; n-1) = valor crítico da distribuição t
- s = desvio padrão amostral
- n = tamanho da amostra

#### Níveis de Confiança
- 90% (α = 0.10)
- 95% (α = 0.05)
- 99% (α = 0.01)

### 4.2 Diferença de Médias (Teste de Welch)

#### Pressupostos
- Normalidade em ambos os grupos
- Independência das observações
- **Não assume** igualdade de variâncias

#### Método
**Estatística t de Welch:**
```
t = (x̄₁ - x̄₂) / √(s₁²/n₁ + s₂²/n₂)
```

**Graus de liberdade (Welch-Satterthwaite):**
```
df = (s₁²/n₁ + s₂²/n₂)² / [(s₁²/n₁)²/(n₁-1) + (s₂²/n₂)²/(n₂-1)]
```

**Intervalo de confiança:**
```
IC(μ₁-μ₂; 1-α) = (x̄₁-x̄₂) ± t(α/2; df) × √(s₁²/n₁ + s₂²/n₂)
```

### 4.3 Intervalos de Confiança para Variâncias

#### Método
**Distribuição Qui-quadrado:**
```
IC(σ²; 1-α) = [(n-1)s²/χ²(α/2; n-1), (n-1)s²/χ²(1-α/2; n-1)]
```

### 4.4 Razão de Variâncias

#### Método
**Distribuição F:**
```
F = s₁²/s₂² (assumindo s₁² ≥ s₂²)
```

**Intervalo de confiança:**
```
IC(σ₁²/σ₂²; 1-α) = [F/F(α/2; n₁-1, n₂-1), F/F(1-α/2; n₁-1, n₂-1)]
```

### 4.5 Proporções

#### Método de Wald
**Intervalo de confiança para proporção:**
```
IC(p; 1-α) = p̂ ± z(α/2) × √[p̂(1-p̂)/n]
```

**Diferença de proporções:**
```
IC(p₁-p₂; 1-α) = (p̂₁-p̂₂) ± z(α/2) × √[p̂₁(1-p̂₁)/n₁ + p̂₂(1-p̂₂)/n₂]
```

---

## 5. Testes de Hipóteses

### 5.1 Teste de Normalidade

#### Shapiro-Wilk (n < 50)
- **H₀:** Os dados seguem distribuição normal
- **H₁:** Os dados não seguem distribuição normal
- **Critério:** Rejeitar H₀ se p-valor < α

#### D'Agostino-Pearson (n ≥ 20)
- Testa simultaneamente assimetria e curtose
- Mais robusto para amostras maiores

### 5.2 Teste de Homogeneidade de Variâncias

#### Teste de Levene
- **H₀:** σ₁² = σ₂² (variâncias iguais)
- **H₁:** σ₁² ≠ σ₂² (variâncias diferentes)
- **Vantagem:** Robusto a desvios da normalidade

### 5.3 Teste de Diferença de Médias

#### Teste t de Welch
- **H₀:** μ₁ = μ₂
- **H₁:** μ₁ ≠ μ₂
- **Escolha:** Preferido quando variâncias são diferentes

#### Mann-Whitney U (não paramétrico)
- **Alternativa:** Quando pressupostos paramétricos não são atendidos
- **H₀:** As distribuições são idênticas

### 5.4 Teste de Diferença de Proporções

#### Teste Z
- **H₀:** p₁ = p₂
- **H₁:** p₁ ≠ p₂

**Estatística de teste:**
```
z = (p̂₁ - p̂₂) / √[p̂(1-p̂)(1/n₁ + 1/n₂)]
```

Onde p̂ = (x₁ + x₂)/(n₁ + n₂) é a proporção pooled.

---

## 6. Análise de Tamanho de Efeito

### Cohen's d (diferença de médias)
```
d = (x̄₁ - x̄₂) / s_pooled
```

Onde s_pooled = √[((n₁-1)s₁² + (n₂-1)s₂²)/(n₁+n₂-2)]

**Interpretação:**
- |d| < 0.2: Efeito pequeno
- 0.2 ≤ |d| < 0.5: Efeito pequeno a médio
- 0.5 ≤ |d| < 0.8: Efeito médio a grande
- |d| ≥ 0.8: Efeito grande

### Cohen's h (diferença de proporções)
```
h = 2[arcsin(√p₁) - arcsin(√p₂)]
```

**Interpretação:** Similar ao Cohen's d

---

## 7. Análise de SLA (Service Level Agreement)

### Definição
SLA = Proporção de atendimentos dentro de um limite de tempo especificado

### Cálculo
```
SLA(t) = P(X ≤ t) = (Número de observações ≤ t) / (Total de observações)
```

### Limites Analisados
- 5 minutos (atendimento rápido)
- 8 minutos (atendimento padrão)
- 10 minutos (atendimento aceitável)

---

## 8. Pressupostos e Limitações

### Pressupostos Atendidos
- ✅ Normalidade dos dados (Shapiro-Wilk: p > 0.05)
- ✅ Independência das observações
- ✅ Amostragem representativa

### Pressupostos Violados
- ❌ Homogeneidade de variâncias (Levene: p = 0.033)
  - **Solução:** Uso do teste de Welch

### Limitações
- Amostra por conveniência (pode haver viés de seleção)
- Período de coleta limitado (não captura sazonalidade)
- Variáveis confundidoras não controladas (horário, região, etc.)

---

## 9. Software e Implementação

### Linguagem
- **Python 3.11+** com bibliotecas científicas

### Bibliotecas Utilizadas
- `numpy`: Cálculos numéricos
- `pandas`: Manipulação de dados
- `scipy.stats`: Testes estatísticos
- `matplotlib/seaborn`: Visualizações

### Reprodutibilidade
- Código versionado no GitHub
- Seed fixo para operações aleatórias
- Documentação completa dos parâmetros

---

## 10. Critérios de Decisão

### Níveis de Significância
- **α = 0.10** (90% de confiança): Evidência moderada
- **α = 0.05** (95% de confiança): Evidência forte
- **α = 0.01** (99% de confiança): Evidência muito forte

### Interpretação de Intervalos
- **Não inclui valor nulo:** Evidência de diferença significativa
- **Inclui valor nulo:** Não há evidência de diferença
- **Amplitude:** Indica precisão da estimativa

### Critérios Práticos
- **Diferença mínima relevante:** 0.5 minutos para tempo de espera
- **Diferença mínima relevante:** 5 pontos percentuais para proporções
- **Consideração do tamanho de efeito:** Além da significância estatística
