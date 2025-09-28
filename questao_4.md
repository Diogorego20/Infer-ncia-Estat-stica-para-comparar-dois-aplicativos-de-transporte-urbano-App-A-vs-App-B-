# QUESTÃO 4 - Razão entre as Variâncias

**Disciplina:** Inferência Estatística I - UFPB CCEN  
**Aluno:** Diogo Da Silva Rego (20240045381)  
**Professora:** Tatiene Correia  
**Tema II:** Transporte Urbano (Comparação entre aplicativos)

---

## Pergunta
**Avaliando a relação entre as variabilidades, qual é a razão entre as variâncias dos aplicativos A e B? Em diferentes níveis de confiança (90%, 95%, 99%), o resultado sugere igualdade ou diferença na consistência entre os aplicativos?**

---

## Metodologia da Razão de Variâncias

### Teste F para Razão de Variâncias
- **Distribuição:** F de Fisher-Snedecor
- **Hipóteses:**
  - H₀: σ₁² = σ₂² (variâncias iguais)
  - H₁: σ₁² ≠ σ₂² (variâncias diferentes)
- **Estatística:** F = s₁²/s₂² (maior variância no numerador)

### Dados das Variâncias
- **App A:** s₁² = 1.147 min² (n₁ = 35)
- **App B:** s₂² = 2.422 min² (n₂ = 55)
- **Razão calculada:** F = s₂²/s₁² = 2.422/1.147 = **2.11**

### Graus de Liberdade
- **Numerador (App B):** df₁ = n₂ - 1 = 54
- **Denominador (App A):** df₂ = n₁ - 1 = 34

---

## Intervalos de Confiança para Razão de Variâncias

### Fórmula
IC(σ₂²/σ₁²; 1-α) = [F/F(α/2; df₁, df₂), F/F(1-α/2; df₁, df₂)]

### Resultados por Nível de Confiança

| Nível | Razão (B/A) | Limite Inferior | Limite Superior | Inclui 1? | Variâncias Iguais? |
|-------|-------------|-----------------|-----------------|-----------|-------------------|
| **90%** | 2.11 | **1.24** | **3.48** | **NÃO** | **NÃO** |
| **95%** | 2.11 | **1.12** | **3.86** | **NÃO** | **NÃO** |
| **99%** | 2.11 | **0.91** | **4.76** | **SIM** | **SIM** |

### Interpretação dos Intervalos

#### 90% de Confiança
- **Intervalo:** [1.24, 3.48]
- **Não inclui 1** → Variâncias são **DIFERENTES**
- **Interpretação:** App B tem variância entre 1.24 e 3.48 vezes maior que App A

#### 95% de Confiança
- **Intervalo:** [1.12, 3.86]
- **Não inclui 1** → Variâncias são **DIFERENTES**
- **Interpretação:** App B tem variância entre 1.12 e 3.86 vezes maior que App A

#### 99% de Confiança
- **Intervalo:** [0.91, 4.76]
- **Inclui 1** → Variâncias podem ser **IGUAIS**
- **Interpretação:** Com 99% de confiança, não há evidência conclusiva de diferença

---

## Teste F Formal

### Estatística de Teste
- **F calculado:** 2.11
- **F crítico (95%):** F₀.₀₂₅(54,34) = 1.89
- **p-valor:** 0.022

### Decisão Estatística
- **F calculado > F crítico** → **Rejeita H₀**
- **p-valor < 0.05** → **Evidência significativa** de diferença

---

## Análise da Razão por Nível

### Resumo dos Resultados

| Nível | Evidência de Diferença | Força da Evidência | Decisão |
|-------|----------------------|-------------------|---------|
| **90%** | ✅ **SIM** | **Forte** | Variâncias diferentes |
| **95%** | ✅ **SIM** | **Moderada** | Variâncias diferentes |
| **99%** | ❌ **NÃO** | **Insuficiente** | Variâncias podem ser iguais |

### Interpretação Prática

#### Níveis 90% e 95%
- **Conclusão:** App B é **significativamente mais variável**
- **Magnitude:** Variância do App B é **mais que o dobro** da do App A
- **Implicação:** Diferença na consistência é **estatisticamente comprovada**

#### Nível 99%
- **Conclusão:** Evidência **não é conclusiva**
- **Explicação:** Nível muito conservador exige evidência muito forte
- **Implicação:** Para decisões práticas, 95% é suficiente

---

## Comparação com Outros Testes

### Consistência dos Resultados

| Teste | Estatística | p-valor | Conclusão (α=0.05) |
|-------|-------------|---------|-------------------|
| **Teste F** | F = 2.11 | 0.022 | Variâncias diferentes |
| **Teste de Levene** | W = 4.63 | 0.033 | Variâncias diferentes |
| **IC para Variâncias** | Não sobrepostos | - | Variâncias diferentes |

### Robustez da Conclusão
- **Múltiplos testes** confirmam a mesma conclusão
- **Evidência convergente** fortalece a confiabilidade
- **Resultado robusto** para decisões práticas

---

## Interpretação da Magnitude

### Razão de Variâncias = 2.11

#### Significado Prático
- App B tem variância **111% maior** que App A
- App B é **2.11 vezes mais variável** que App A
- **Diferença substancial** na previsibilidade

#### Classificação da Diferença
| Razão | Classificação | Interpretação |
|-------|---------------|---------------|
| 1.0 - 1.5 | Pequena | Diferença mínima |
| 1.5 - 2.0 | Moderada | Diferença notável |
| **2.0 - 3.0** | **Grande** | **Diferença substancial** |
| > 3.0 | Muito Grande | Diferença extrema |

### Impacto na Experiência
- **Fator 2.11** representa diferença **muito perceptível** para usuários
- **Variabilidade dobrada** afeta significativamente a previsibilidade
- **Impacto operacional** relevante para gestão do serviço

---

## Análise de Sensibilidade

### Comportamento por Nível de Confiança

#### Padrão Observado
- **90%:** Evidência forte de diferença
- **95%:** Evidência moderada de diferença  
- **99%:** Evidência insuficiente

#### Explicação Estatística
- **Aumento do nível** → **Intervalos mais largos** → **Maior chance de incluir 1**
- **Trade-off:** Confiança vs Precisão
- **Ponto de inflexão:** Entre 95% e 99%

### Recomendação Metodológica
- **Para decisões práticas:** Usar 95% de confiança
- **Para pesquisa acadêmica:** Considerar 90% e 95%
- **Para decisões críticas:** Avaliar contexto específico

---

## Conclusão

### Resposta à Pergunta Principal

**A razão entre as variâncias é 2.11**, indicando que o **App B é mais que duas vezes mais variável** que o App A.

### Resultado por Nível de Confiança

1. **90% e 95%:** **DIFERENÇA** significativa na consistência
2. **99%:** **IGUALDADE** não pode ser descartada

### Interpretação Final

#### Evidência Estatística
- **Forte evidência** (90% e 95%) de que os aplicativos têm consistências **diferentes**
- **App A é significativamente mais consistente** que App B
- **Diferença é substancial** (fator 2.11) e **praticamente relevante**

#### Implicação para Gestão
- **Diferença na consistência** é **estatisticamente comprovada**
- **App A oferece serviço mais previsível**
- **Decisão deve considerar** trade-off entre velocidade (App B) e consistência (App A)

### Recomendação
Para **níveis práticos de confiança** (90% e 95%), há **evidência clara** de que os aplicativos têm **consistências diferentes**, com **App A sendo significativamente mais previsível**.
