# QUESTÃO 2 - Diferença entre as Médias

**Disciplina:** Inferência Estatística I - UFPB CCEN  
**Aluno:** Diogo Da Silva Rego (20240045381)  
**Professora:** Tatiene Correia  
**Tema II:** Transporte Urbano (Comparação entre aplicativos)

---

## Pergunta
**Considerando a diferença entre as médias de tempo de espera (A - B), qual é a estimativa dessa diferença? O intervalo sugere diferença significativa entre os tempos médios em 90%, 95% e 99%?**

---

## Metodologia Aplicada

### Teste de Welch (Variâncias Diferentes)
- **Justificativa:** Teste de Levene indicou variâncias heterogêneas (p = 0.033)
- **Vantagem:** Não assume igualdade de variâncias
- **Fórmula:** t = (x̄₁ - x̄₂) / √(s₁²/n₁ + s₂²/n₂)

### Graus de Liberdade (Welch-Satterthwaite)
```
df = (s₁²/n₁ + s₂²/n₂)² / [(s₁²/n₁)²/(n₁-1) + (s₂²/n₂)²/(n₂-1)]
df = 82.47
```

---

## Resultados dos Intervalos de Confiança

### Diferença de Médias (App A - App B)

| Nível de Confiança | Diferença | Margem de Erro | Limite Inferior | Limite Superior | Significativo? |
|-------------------|-----------|----------------|-----------------|-----------------|----------------|
| **90%** | 0.623 min | 0.461 min | **0.162 min** | **1.084 min** | **SIM** |
| **95%** | 0.623 min | 0.551 min | **0.072 min** | **1.174 min** | **SIM** |
| **99%** | 0.623 min | 0.730 min | **-0.107 min** | **1.353 min** | **NÃO** |

**Estatística t de Welch:** t = 2.248  
**p-valor:** 0.027

---

## Interpretação da Significância

### Critério de Significância
Um intervalo de confiança **não inclui zero** → diferença é **estatisticamente significativa**

### Análise por Nível

#### 90% de Confiança
- **Intervalo:** [0.162, 1.084] minutos
- **Não inclui zero** → **DIFERENÇA SIGNIFICATIVA**
- **Interpretação:** App A demora entre 0.16 e 1.08 min a mais que App B

#### 95% de Confiança
- **Intervalo:** [0.072, 1.174] minutos
- **Não inclui zero** → **DIFERENÇA SIGNIFICATIVA**
- **Interpretação:** App A demora entre 0.07 e 1.17 min a mais que App B
- **Margem pequena:** Limite inferior próximo de zero indica evidência moderada

#### 99% de Confiança
- **Intervalo:** [-0.107, 1.353] minutos
- **Inclui zero** → **DIFERENÇA NÃO SIGNIFICATIVA**
- **Interpretação:** Com 99% de confiança, não podemos afirmar que há diferença

---

## Teste de Hipóteses Complementar

### Hipóteses
- **H₀:** μ₁ = μ₂ (não há diferença entre as médias)
- **H₁:** μ₁ ≠ μ₂ (há diferença entre as médias)

### Resultado
- **Estatística t:** 2.248
- **p-valor:** 0.027
- **Conclusão:** Rejeita-se H₀ ao nível α = 0.05

### Interpretação do p-valor
- **p = 0.027 < 0.05** → Evidência **forte** contra H₀
- **p = 0.027 < 0.10** → Evidência **muito forte** contra H₀
- **p = 0.027 > 0.01** → Evidência **não conclusiva** ao nível 1%

---

## Tamanho do Efeito (Cohen's d)

### Cálculo
```
d = (x̄₁ - x̄₂) / s_pooled = 0.623 / 1.387 = 0.449
```

### Interpretação
- **d = 0.449** → Efeito **pequeno a médio**
- **Relevância prática:** A diferença não é apenas estatística, mas também praticamente relevante

---

## Síntese dos Resultados

### Evidência Estatística
| Nível | Significativo | Força da Evidência |
|-------|---------------|-------------------|
| **90%** | ✅ Sim | Forte |
| **95%** | ✅ Sim | Moderada |
| **99%** | ❌ Não | Insuficiente |

### Consistência dos Resultados
- **Teste t de Welch:** p = 0.027 (significativo a 5%)
- **Intervalos de confiança:** Confirmam significância até 95%
- **Tamanho de efeito:** Moderadamente relevante (d = 0.449)

---

## Conclusão

### Resposta à Pergunta
**SIM**, há evidência de diferença significativa entre os tempos médios dos aplicativos em **90% e 95%** de confiança, mas **NÃO** em 99%.

### Interpretação Prática
1. **App B é mais rápido:** Diferença média de 0.62 minutos (37 segundos)
2. **Evidência robusta:** Confirmada por múltiplos testes estatísticos
3. **Relevância prática:** Diferença é estatística e praticamente significativa
4. **Limitação:** Em níveis muito conservadores (99%), a evidência não é conclusiva

### Recomendação
Para **decisões práticas**, a evidência a **95% de confiança** é suficiente para concluir que o **App B tem tempo médio menor** que o App A.
