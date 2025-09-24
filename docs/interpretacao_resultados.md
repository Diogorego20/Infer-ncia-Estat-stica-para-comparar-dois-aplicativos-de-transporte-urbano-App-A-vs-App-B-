# Interpretação dos Resultados

**Projeto:** Análise Comparativa de Aplicativos de Transporte Urbano  
**Autor:** Diogo Da Silva Rego  
**Data:** 23 de Setembro de 2025

---

## Visão Geral

Este documento fornece orientações detalhadas para interpretação dos resultados da análise estatística, explicando o significado prático de cada métrica e teste realizado.

---

## 1. Interpretação de Intervalos de Confiança

### 1.1 Conceito Fundamental

Um **intervalo de confiança de 95%** significa que, se repetíssemos o processo de amostragem muitas vezes, 95% dos intervalos construídos conteriam o verdadeiro valor do parâmetro populacional.

### 1.2 Componentes do Intervalo

#### Margem de Erro
- **Definição:** Metade da amplitude do intervalo
- **Interpretação:** Máximo erro esperado na estimativa
- **Exemplo:** ME = 0.37 min significa que a média verdadeira está a ±0.37 min da estimativa

#### Amplitude
- **Definição:** Largura total do intervalo (2 × Margem de Erro)
- **Interpretação:** Indica a precisão da estimativa
- **Regra:** Amplitude menor = estimativa mais precisa

### 1.3 Interpretação por Nível de Confiança

| Nível | Interpretação | Uso Recomendado |
|-------|---------------|-----------------|
| **90%** | Evidência moderada | Decisões operacionais |
| **95%** | Evidência forte | Decisões estratégicas |
| **99%** | Evidência muito forte | Decisões críticas |

---

## 2. Interpretação de Testes de Hipóteses

### 2.1 p-valor

#### Definição
Probabilidade de observar um resultado tão extremo quanto o obtido, assumindo que a hipótese nula é verdadeira.

#### Interpretação Prática

| p-valor | Interpretação | Força da Evidência |
|---------|---------------|-------------------|
| p ≥ 0.10 | Não há evidência contra H₀ | Nenhuma |
| 0.05 ≤ p < 0.10 | Evidência fraca contra H₀ | Fraca |
| 0.01 ≤ p < 0.05 | Evidência forte contra H₀ | Forte |
| p < 0.01 | Evidência muito forte contra H₀ | Muito forte |

#### Exemplo Prático
- **p = 0.027** para diferença de médias
- **Interpretação:** Há apenas 2.7% de chance de observar uma diferença tão grande por acaso
- **Conclusão:** Evidência forte de que as médias são diferentes

### 2.2 Significância Estatística vs. Prática

#### Significância Estatística
- **Critério:** p-valor < α (geralmente 0.05)
- **Significado:** Resultado improvável de ser devido ao acaso

#### Significância Prática
- **Critério:** Magnitude do efeito é relevante para o contexto
- **Exemplo:** Diferença de 0.62 min pode ser estatisticamente significativa, mas pode não ser praticamente relevante para usuários

---

## 3. Interpretação de Métricas Específicas

### 3.1 Tempo Médio de Espera

#### Resultados Obtidos
- **App A:** 7.43 ± 0.37 min (IC 95%)
- **App B:** 6.81 ± 0.42 min (IC 95%)

#### Interpretação
1. **App B é mais rápido:** Diferença de 0.62 min (37 segundos)
2. **Incerteza maior no App B:** Margem de erro 14% maior
3. **Sobreposição dos ICs:** Mínima, indicando diferença real

#### Implicações Práticas
- Usuários do App B esperam menos tempo **na média**
- Maior variabilidade no App B pode gerar experiências inconsistentes
- Diferença de 37 segundos pode ser relevante em contextos urbanos

### 3.2 Variabilidade (Coeficiente de Variação)

#### Resultados Obtidos
- **App A:** CV = 14.4%
- **App B:** CV = 22.9%

#### Interpretação
1. **App A é 38% mais consistente** que App B
2. **Previsibilidade:** App A oferece experiência mais uniforme
3. **Risco operacional:** App B tem maior variabilidade

#### Classificação da Variabilidade
| CV | Classificação | Interpretação |
|----|---------------|---------------|
| < 15% | Baixa | Serviço muito consistente |
| 15-25% | Moderada | Serviço razoavelmente consistente |
| > 25% | Alta | Serviço inconsistente |

### 3.3 Proporções de Aprovação

#### Resultados Obtidos
- **App A:** 88% ± 5.2% (IC 95%)
- **App B:** 80% ± 6.4% (IC 95%)

#### Interpretação
1. **App A tem maior aprovação:** 8 pontos percentuais de diferença
2. **Significância:** Depende do nível de confiança escolhido
3. **Relevância prática:** 8 p.p. é uma diferença substancial

#### Contexto de Satisfação
| Aprovação | Classificação | Ação Recomendada |
|-----------|---------------|-------------------|
| > 85% | Excelente | Manter padrão |
| 70-85% | Boa | Melhorias pontuais |
| < 70% | Insatisfatória | Ação corretiva urgente |

---

## 4. Interpretação de SLA (Service Level Agreement)

### 4.1 Conceito
SLA mede o percentual de atendimentos que cumprem uma meta de tempo específica.

### 4.2 Resultados por Limite

#### SLA 5 minutos (Atendimento Rápido)
- **App A:** 0.0%
- **App B:** 10.9%
- **Interpretação:** App B é superior para demandas urgentes

#### SLA 8 minutos (Atendimento Padrão)
- **App A:** 65.7%
- **App B:** 76.4%
- **Interpretação:** App B atende melhor expectativas padrão

#### SLA 10 minutos (Atendimento Aceitável)
- **App A:** 100.0%
- **App B:** 98.2%
- **Interpretação:** App A garante atendimento universal

### 4.3 Implicações Estratégicas

#### Para Metas Agressivas (≤ 8 min)
- **Escolha:** App B
- **Justificativa:** Melhor performance em tempos curtos

#### Para Garantia de Serviço (≤ 10 min)
- **Escolha:** App A
- **Justificativa:** Atendimento universal garantido

---

## 5. Interpretação da Análise de Variâncias

### 5.1 Teste de Levene (Homogeneidade)

#### Resultado
- **p-valor = 0.033**
- **Conclusão:** Variâncias são diferentes (p < 0.05)

#### Implicação Metodológica
- **Recomendação:** Usar teste de Welch (não assume variâncias iguais)
- **Evitar:** Teste t de Student clássico

### 5.2 Razão de Variâncias (A/B)

#### Resultados por Nível
- **90%:** [0.288, 0.806] - Não inclui 1 → Variâncias diferentes
- **95%:** [0.261, 0.895] - Não inclui 1 → Variâncias diferentes  
- **99%:** [0.217, 1.103] - Inclui 1 → Variâncias podem ser iguais

#### Interpretação
1. **Evidência forte** (95%) de que App B é mais variável
2. **Razão = 0.473:** App A tem menos da metade da variância do App B
3. **Consistência:** App A é significativamente mais previsível

---

## 6. Interpretação do Tamanho de Efeito

### 6.1 Cohen's d (Diferença de Médias)

#### Resultado
- **d = 0.449**
- **Classificação:** Efeito pequeno a médio

#### Interpretação Prática
- A diferença entre as médias é **moderadamente relevante**
- Não é apenas significância estatística, mas também prática
- Justifica consideração na tomada de decisão

### 6.2 Cohen's h (Diferença de Proporções)

#### Resultado
- **h = 0.220**
- **Classificação:** Efeito pequeno a médio

#### Interpretação
- Diferença de aprovação é **moderadamente relevante**
- Pode impactar percepção pública do serviço
- Relevante para decisões de política pública

---

## 7. Interpretação Integrada

### 7.1 Trade-off Identificado

#### Velocidade vs. Consistência
- **App B:** Mais rápido, mas menos previsível
- **App A:** Mais lento, mas mais consistente
- **Decisão:** Depende da prioridade estratégica

#### Matriz de Decisão

| Prioridade | App Recomendado | Justificativa |
|------------|-----------------|---------------|
| **Velocidade média** | App B | Tempo médio menor |
| **Previsibilidade** | App A | Menor variabilidade |
| **Satisfação usuário** | App A | Maior aprovação |
| **SLA agressivo** | App B | Melhor performance < 8 min |
| **Garantia universal** | App A | 100% atendimento < 10 min |

### 7.2 Robustez dos Resultados

#### Consistência entre Testes
- **Paramétricos e não-paramétricos:** Resultados concordantes
- **Múltiplos níveis de confiança:** Padrão consistente
- **Diferentes métricas:** Confirmam o trade-off

#### Confiabilidade
- **Alta:** Resultados são estatisticamente robustos
- **Reprodutível:** Metodologia bem documentada
- **Válida:** Pressupostos verificados

---

## 8. Limitações da Interpretação

### 8.1 Limitações Estatísticas

#### Amostragem
- **Conveniência:** Pode haver viés de seleção
- **Período limitado:** Não captura sazonalidade
- **Tamanho:** Amostras relativamente pequenas

#### Variáveis Confundidoras
- **Não controladas:** Horário, região, tipo de usuário
- **Impacto:** Pode influenciar resultados
- **Mitigação:** Interpretação cautelosa

### 8.2 Limitações Práticas

#### Contexto Específico
- **Cidade específica:** Resultados podem não ser generalizáveis
- **Período específico:** Condições podem ter mudado
- **Aplicativos específicos:** Outros apps podem ter performance diferente

#### Fatores Não Mensurados
- **Qualidade do veículo:** Não avaliada
- **Atendimento do motorista:** Não mensurado
- **Preço:** Não considerado na análise

---

## 9. Recomendações para Uso dos Resultados

### 9.1 Para Gestores Públicos

#### Decisões Estratégicas
- **Usar IC 95%** para decisões importantes
- **Considerar tamanho de efeito** além da significância
- **Avaliar trade-offs** entre métricas

#### Monitoramento
- **Acompanhar tendências** ao longo do tempo
- **Reavaliar periodicamente** com novos dados
- **Considerar fatores externos** que podem influenciar

### 9.2 Para Análises Futuras

#### Melhorias Metodológicas
- **Amostragem aleatória** para reduzir viés
- **Período mais longo** para capturar variabilidade
- **Controle de variáveis** confundidoras

#### Métricas Adicionais
- **Satisfação detalhada** (escala Likert)
- **Análise de custos** operacionais
- **Impacto ambiental** dos serviços

---

## 10. Conclusões da Interpretação

### 10.1 Principais Insights

1. **Trade-off claro:** Velocidade vs. Consistência
2. **Evidência robusta:** Resultados estatisticamente sólidos
3. **Relevância prática:** Diferenças são significativas para usuários
4. **Decisão contextual:** Escolha depende de prioridades estratégicas

### 10.2 Valor da Análise

#### Para a Organização
- **Base científica** para decisões
- **Quantificação** de trade-offs
- **Redução de incerteza** na escolha

#### Para os Usuários
- **Melhoria** na qualidade do serviço
- **Transparência** no processo decisório
- **Consideração** de suas preferências
