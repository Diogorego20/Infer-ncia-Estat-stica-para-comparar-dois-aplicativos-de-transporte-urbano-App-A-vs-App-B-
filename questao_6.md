# QUESTÃO 6 - Diferença entre as Proporções

**Disciplina:** Inferência Estatística I - UFPB CCEN  
**Aluno:** Diogo Da Silva Rego (20240045381)  
**Professora:** Tatiene Correia  
**Tema II:** Transporte Urbano (Comparação entre aplicativos)

---

## Pergunta
**Considerando a diferença entre as proporções de aprovação (A - B), qual é a estimativa dessa diferença? Em diferentes níveis de confiança (90%, 95%, 99%), o intervalo inclui ou não o valor zero? O que isso indica sobre a aceitação das duas marcas no mercado?**

---

## Metodologia para Diferença de Proporções

### Dados Base
- **App A:** p̂₁ = 132/150 = 0.880 (88.0%)
- **App B:** p̂₂ = 120/150 = 0.800 (80.0%)
- **Diferença observada:** p̂₁ - p̂₂ = 0.080 (8.0 pontos percentuais)

### Método de Wald para Diferença
**Fórmula:** IC(p₁-p₂; 1-α) = (p̂₁-p̂₂) ± z(α/2) × √[p̂₁(1-p̂₁)/n₁ + p̂₂(1-p̂₂)/n₂]

### Cálculo do Erro Padrão
```
SE = √[p̂₁(1-p̂₁)/n₁ + p̂₂(1-p̂₂)/n₂]
SE = √[0.880×0.120/150 + 0.800×0.200/150]
SE = √[0.000704 + 0.001067] = √0.001771 = 0.0421
```

---

## Intervalos de Confiança para Diferença

### Resultados por Nível de Confiança

| Nível | Diferença | Margem de Erro | Limite Inferior | Limite Superior | Inclui Zero? | Significativo? |
|-------|-----------|----------------|-----------------|-----------------|--------------|----------------|
| **90%** | 0.080 | **0.069** | **0.011** | **0.149** | **NÃO** | **SIM** |
| **95%** | 0.080 | **0.082** | **-0.002** | **0.162** | **SIM** | **NÃO** |
| **99%** | 0.080 | **0.108** | **-0.028** | **0.188** | **SIM** | **NÃO** |

### Valores Críticos Utilizados
- **90%:** z₀.₀₅ = 1.645
- **95%:** z₀.₀₂₅ = 1.960  
- **99%:** z₀.₀₀₅ = 2.576

---

## Interpretação por Nível de Confiança

### 90% de Confiança
- **Intervalo:** [0.011, 0.149] ou [1.1%, 14.9%]
- **Não inclui zero** → **DIFERENÇA SIGNIFICATIVA**
- **Interpretação:** App A tem entre 1.1 e 14.9 pontos percentuais a mais de aprovação
- **Conclusão:** Evidência **forte** de superioridade do App A

### 95% de Confiança
- **Intervalo:** [-0.002, 0.162] ou [-0.2%, 16.2%]
- **Inclui zero** → **DIFERENÇA NÃO SIGNIFICATIVA**
- **Interpretação:** A diferença pode ser de -0.2% a +16.2%
- **Conclusão:** Evidência **insuficiente** para afirmar superioridade
- **Observação:** Limite inferior muito próximo de zero (-0.2%)

### 99% de Confiança
- **Intervalo:** [-0.028, 0.188] ou [-2.8%, 18.8%]
- **Inclui zero** → **DIFERENÇA NÃO SIGNIFICATIVA**
- **Interpretação:** A diferença pode ser de -2.8% a +18.8%
- **Conclusão:** Evidência **insuficiente** para conclusões definitivas

---

## Teste de Hipóteses Complementar

### Teste Z para Diferença de Proporções

#### Hipóteses
- **H₀:** p₁ = p₂ (não há diferença entre as proporções)
- **H₁:** p₁ ≠ p₂ (há diferença entre as proporções)

#### Método com Proporção Pooled
```
p̂_pooled = (x₁ + x₂)/(n₁ + n₂) = (132 + 120)/(150 + 150) = 0.840
SE_pooled = √[0.840 × 0.160 × (1/150 + 1/150)] = 0.0424
z = (0.880 - 0.800)/0.0424 = 1.887
```

#### Resultado
- **Estatística Z:** 1.887
- **p-valor:** 0.059
- **Interpretação:** Marginalmente significativo

---

## Análise da Significância

### Resumo por Nível

| Nível | Critério | Resultado | Interpretação |
|-------|----------|-----------|---------------|
| **90%** | Não inclui 0 | **SIGNIFICATIVO** | Evidência forte |
| **95%** | Inclui 0 | **NÃO SIGNIFICATIVO** | Evidência marginal |
| **99%** | Inclui 0 | **NÃO SIGNIFICATIVO** | Evidência insuficiente |

### Padrão Observado
- **Significância decresce** com aumento do nível de confiança
- **Evidência marginal:** p-valor = 0.059 (próximo de 0.05)
- **Resultado limítrofe:** Entre significativo e não significativo

---

## O que Isso Indica sobre Aceitação no Mercado?

### 1. Interpretação da Significância Marginal

#### Evidência Moderada
- **90% de confiança:** Há diferença real entre os apps
- **95% de confiança:** Diferença pode ser devida ao acaso
- **Conclusão:** Evidência **moderada** de superioridade do App A

#### Implicação Prática
- **Diferença existe** mas **não é esmagadora**
- **Vantagem do App A** é **real mas moderada**
- **Mercado:** Ambos os apps têm aceitação razoável

### 2. Análise da Magnitude

#### Diferença de 8 Pontos Percentuais
- **Relevância prática:** Diferença **substancial** em pesquisas de satisfação
- **Contexto de mercado:** 8% pode representar milhares de usuários
- **Impacto comercial:** Diferença **comercialmente relevante**

#### Comparação com Benchmarks
| Diferença | Classificação | Interpretação |
|-----------|---------------|---------------|
| 0-3% | Pequena | Diferença mínima |
| 3-7% | Moderada | Diferença notável |
| **7-15%** | **Grande** | **Diferença substancial** |
| >15% | Muito Grande | Diferença extrema |

### 3. Posicionamento no Mercado

#### App A (88% de aprovação)
- **Posição:** **Líder de satisfação**
- **Vantagem competitiva:** Serviço mais consistente e aprovado
- **Estratégia:** Manter qualidade e explorar diferencial

#### App B (80% de aprovação)
- **Posição:** **Competidor forte**
- **Desafio:** Melhorar consistência para alcançar App A
- **Oportunidade:** Ainda tem boa aceitação (80%)

### 4. Dinâmica Competitiva

#### Cenário de Mercado
- **Não há dominância absoluta:** Diferença não é esmagadora
- **Competição saudável:** Ambos têm aceitação boa/excelente
- **Oportunidade de melhoria:** App B pode reduzir gap

#### Fatores de Diferenciação
- **App A:** Foca em **consistência e previsibilidade**
- **App B:** Foca em **velocidade média**
- **Mercado:** Valoriza mais consistência que velocidade

---

## Implicações Estratégicas

### Para o Gestor Público

#### Cenário de Decisão
- **Vantagem moderada** do App A
- **Não há app claramente superior** em todos os aspectos
- **Decisão complexa:** Considerar múltiplos fatores

#### Estratégias Possíveis

##### Estratégia 1: Priorizar App A
- **Justificativa:** Maior aprovação e consistência
- **Risco:** Perder velocidade média
- **Adequado para:** Foco em satisfação do usuário

##### Estratégia 2: Modelo Híbrido
- **Justificativa:** Aproveitar pontos fortes de ambos
- **Implementação:** Incentivos diferenciados
- **Adequado para:** Maximizar benefícios

##### Estratégia 3: Competição Saudável
- **Justificativa:** Manter ambos para estimular melhoria
- **Implementação:** Metas de performance
- **Adequado para:** Evolução contínua

### Para os Aplicativos

#### App A
- **Manter vantagem:** Preservar consistência
- **Oportunidade:** Melhorar velocidade sem perder qualidade
- **Estratégia:** Consolidar liderança em satisfação

#### App B
- **Reduzir gap:** Melhorar consistência
- **Manter força:** Preservar velocidade
- **Estratégia:** Equilibrar velocidade e previsibilidade

---

## Conclusão

### Resposta às Perguntas

1. **Estimativa da diferença:** 8.0 pontos percentuais (App A - App B)
2. **Inclusão do zero:**
   - **90%:** NÃO inclui → Significativo
   - **95%:** SIM inclui → Não significativo  
   - **99%:** SIM inclui → Não significativo
3. **Aceitação no mercado:** Vantagem **moderada** do App A

### Interpretação Final

#### Sobre a Diferença
- **Existe diferença real** entre os apps (evidência a 90%)
- **Diferença é moderada** (8 pontos percentuais)
- **Não é estatisticamente robusta** a 95% (p = 0.059)

#### Sobre o Mercado
- **App A tem vantagem competitiva** em satisfação
- **Vantagem não é esmagadora** - mercado competitivo
- **Ambos têm boa aceitação** (80% e 88%)
- **Diferenciação por atributos:** Consistência vs Velocidade

#### Recomendação
A **diferença marginal** sugere um **mercado equilibrado** onde o **App A tem ligeira vantagem** em satisfação, mas **ambos são viáveis**. A decisão deve considerar **objetivos estratégicos específicos** além da aprovação dos usuários.
