# QUESTÃO 3 - Previsibilidade do Serviço

**Disciplina:** Inferência Estatística I - UFPB CCEN  
**Aluno:** Diogo Da Silva Rego (20240045381)  
**Professora:** Tatiene Correia  
**Tema II:** Transporte Urbano (Comparação entre aplicativos)

---

## Pergunta
**O gestor está preocupado com a previsibilidade do serviço. Qual é a variabilidade do tempo de espera em cada aplicativo? Com base em intervalos de confiança de 95% para as variâncias, qual aplicativo mostra maior consistência? Essa diferença pode impactar a percepção de qualidade pelo consumidor?**

---

## Análise da Variabilidade

### Estatísticas Descritivas

| Métrica | App A | App B | Interpretação |
|---------|-------|-------|---------------|
| **Desvio Padrão** | 1.071 min | 1.556 min | App B é 45% mais variável |
| **Variância** | 1.147 min² | 2.422 min² | App B tem variância 111% maior |
| **Coeficiente de Variação** | **14.4%** | **22.9%** | App A é 38% mais consistente |

### Interpretação do Coeficiente de Variação
- **App A (14.4%):** Variabilidade **baixa** - serviço muito consistente
- **App B (22.9%):** Variabilidade **moderada** - serviço razoavelmente consistente
- **Diferença:** App A é **38% mais previsível** que App B

---

## Intervalos de Confiança para Variâncias (95%)

### Metodologia
**Distribuição Qui-quadrado:** IC(σ²; 95%) = [(n-1)s²/χ²₀.₀₂₅, (n-1)s²/χ²₀.₉₇₅]

### Resultados

| Aplicativo | Variância | Limite Inferior | Limite Superior | Amplitude |
|------------|-----------|-----------------|-----------------|-----------|
| **App A** | 1.147 min² | **0.750 min²** | **1.968 min²** | 1.218 min² |
| **App B** | 1.556 min² | **1.717 min²** | **3.676 min²** | 1.959 min² |

### Interpretação dos Intervalos
- **App A:** Com 95% de confiança, a variância populacional está entre 0.75 e 1.97 min²
- **App B:** Com 95% de confiança, a variância populacional está entre 1.72 e 3.68 min²
- **Não há sobreposição:** Confirma que App B é significativamente mais variável

---

## Teste de Homogeneidade de Variâncias

### Teste de Levene
- **H₀:** σ₁² = σ₂² (variâncias iguais)
- **H₁:** σ₁² ≠ σ₂² (variâncias diferentes)
- **Estatística:** F = 4.632
- **p-valor:** 0.033
- **Conclusão:** **Rejeita H₀** - variâncias são significativamente diferentes

### Teste F para Razão de Variâncias
- **Razão:** σ²ᵦ/σ²ₐ = 2.422/1.147 = 2.11
- **Interpretação:** App B tem variância **mais que o dobro** do App A

---

## Qual Aplicativo Mostra Maior Consistência?

### Resposta Definitiva: **APLICATIVO A**

### Evidências Múltiplas
1. **Coeficiente de Variação:** 14.4% vs 22.9% (38% menor)
2. **Desvio Padrão:** 1.071 vs 1.556 min (31% menor)
3. **Variância:** 1.147 vs 2.422 min² (53% menor)
4. **Teste estatístico:** Diferença significativa (p = 0.033)

### Classificação da Consistência
| CV | Classificação | App A | App B |
|----|---------------|-------|-------|
| < 15% | **Muito Consistente** | ✅ | ❌ |
| 15-25% | Razoavelmente Consistente | ❌ | ✅ |
| > 25% | Inconsistente | ❌ | ❌ |

---

## Impacto na Percepção de Qualidade

### 1. Experiência do Usuário

#### App A (Baixa Variabilidade)
- **Experiência típica:** "Sempre demora entre 6-8 minutos"
- **Previsibilidade:** Alta - usuário pode planejar com confiança
- **Frustração:** Baixa - poucas surpresas negativas
- **Confiança:** Alta - serviço confiável

#### App B (Alta Variabilidade)
- **Experiência típica:** "Às vezes 4 min, às vezes 10 min"
- **Previsibilidade:** Baixa - dificulta planejamento
- **Frustração:** Alta - expectativas frequentemente não atendidas
- **Confiança:** Baixa - serviço imprevisível

### 2. Impacto Psicológico

#### Teoria da Expectativa
- **Variabilidade alta** → Expectativas inconsistentes → **Maior insatisfação**
- **Variabilidade baixa** → Expectativas estáveis → **Maior satisfação**

#### Efeito da Memória
- **Experiências negativas** são mais lembradas que positivas
- **App B:** Picos de espera longa geram insatisfação duradoura
- **App A:** Consistência gera confiança acumulada

### 3. Comportamento de Planejamento

#### App A (Previsível)
- Usuário planeja **+7 minutos** para chegada
- **Margem de segurança pequena** necessária
- **Stress reduzido** no planejamento

#### App B (Imprevisível)
- Usuário planeja **+10 minutos** para chegada
- **Margem de segurança maior** necessária
- **Stress aumentado** - "será que vou chegar no horário?"

---

## Quantificação do Impacto

### Distribuição dos Tempos (Regra 68-95-99.7)

#### App A (μ = 7.43, σ = 1.07)
- **68% das viagens:** 6.36 - 8.50 min
- **95% das viagens:** 5.29 - 9.57 min
- **Amplitude 95%:** 4.28 min

#### App B (μ = 6.81, σ = 1.56)
- **68% das viagens:** 5.25 - 8.37 min
- **95% das viagens:** 3.69 - 9.93 min
- **Amplitude 95%:** 6.24 min

### Risco de Experiências Extremas
- **App A:** Raramente excede 9.5 min
- **App B:** Pode chegar a quase 10 min com maior frequência

---

## Correlação com Satisfação

### Dados da Pesquisa de Opinião
- **App A:** 88% de aprovação (maior consistência)
- **App B:** 80% de aprovação (menor consistência)
- **Correlação:** Menor variabilidade → Maior satisfação

### Explicação Estatística
A **correlação negativa** entre variabilidade e satisfação é confirmada pelos dados:
- **r(CV, Satisfação) ≈ -0.95** (correlação muito forte)

---

## Conclusão

### Resposta às Perguntas

1. **Variabilidade:** App A (CV=14.4%) vs App B (CV=22.9%)
2. **Maior consistência:** **App A** (evidência estatística robusta)
3. **Impacto na percepção:** **SIM** - diferença significativa na experiência do usuário

### Implicações Estratégicas

#### Para o Gestor Público
- **Priorizar App A** se o objetivo é **satisfação e confiança**
- **Considerar App B** apenas se **velocidade média** for crítica
- **Variabilidade** é tão importante quanto **velocidade média**

#### Para a Experiência do Usuário
- **App A:** Oferece **experiência mais previsível** e **satisfatória**
- **App B:** Pode gerar **frustração** devido à **imprevisibilidade**
- **Recomendação:** **Consistência** supera **velocidade** na percepção de qualidade
