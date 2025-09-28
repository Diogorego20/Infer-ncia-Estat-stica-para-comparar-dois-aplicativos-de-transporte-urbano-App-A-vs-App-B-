# QUESTÃO 5 - Proporção de Aprovação

**Disciplina:** Inferência Estatística I - UFPB CCEN  
**Aluno:** Diogo Da Silva Rego (20240045381)  
**Professora:** Tatiene Correia  
**Tema II:** Transporte Urbano (Comparação entre aplicativos)

---

## Pergunta
**Na pesquisa de opinião, qual é a estimativa da proporção de aprovação de cada app? Qual a margem de erro em 90%, 95% e 99%? Qual app se mostra mais aceito pelo público? Justifique.**

---

## Dados da Pesquisa de Opinião

### Amostra Coletada
- **Total de usuários:** 300 (150 por aplicativo)
- **Método:** Amostragem aleatória estratificada
- **Pergunta:** "Você aprova o serviço do aplicativo?"

### Resultados Brutos
- **App A:** 132 aprovações em 150 usuários
- **App B:** 120 aprovações em 150 usuários

---

## Cálculo das Proporções

### Proporções Amostrais
- **App A:** p̂₁ = 132/150 = **0.880** (88.0%)
- **App B:** p̂₂ = 120/150 = **0.800** (80.0%)
- **Diferença:** p̂₁ - p̂₂ = 0.080 (8.0 pontos percentuais)

---

## Intervalos de Confiança para Proporções

### Metodologia (Método de Wald)
**Fórmula:** IC(p; 1-α) = p̂ ± z(α/2) × √[p̂(1-p̂)/n]

### Aplicativo A (88.0% de aprovação)

| Nível | Proporção | Margem de Erro | Amplitude | Limite Inferior | Limite Superior |
|-------|-----------|----------------|-----------|-----------------|-----------------|
| **90%** | 0.880 | **0.044** | 0.088 | **0.836** | **0.924** |
| **95%** | 0.880 | **0.052** | 0.104 | **0.828** | **0.932** |
| **99%** | 0.880 | **0.068** | 0.136 | **0.812** | **0.948** |

**Erro padrão:** SE = √[0.880 × 0.120 / 150] = 0.0265

### Aplicativo B (80.0% de aprovação)

| Nível | Proporção | Margem de Erro | Amplitude | Limite Inferior | Limite Superior |
|-------|-----------|----------------|-----------|-----------------|-----------------|
| **90%** | 0.800 | **0.054** | 0.108 | **0.746** | **0.854** |
| **95%** | 0.800 | **0.064** | 0.128 | **0.736** | **0.864** |
| **99%** | 0.800 | **0.084** | 0.168 | **0.716** | **0.884** |

**Erro padrão:** SE = √[0.800 × 0.200 / 150] = 0.0327

---

## Comparação das Margens de Erro

### Análise da Precisão

| Nível | Margem de Erro A | Margem de Erro B | Diferença | App Mais Preciso |
|-------|------------------|------------------|-----------|------------------|
| **90%** | 4.4% | 5.4% | +1.0% | **App A** |
| **95%** | 5.2% | 6.4% | +1.2% | **App A** |
| **99%** | 6.8% | 8.4% | +1.6% | **App A** |

### Explicação da Diferença
- **App A tem menor margem de erro** em todos os níveis
- **Causa:** Proporção mais próxima dos extremos (0 ou 1) tem menor variabilidade
- **Fórmula:** Variância máxima ocorre em p = 0.5

---

## Qual App é Mais Aceito?

### Resposta: **APLICATIVO A**

### Evidências Quantitativas

#### 1. Proporção Pontual
- **App A:** 88.0% de aprovação
- **App B:** 80.0% de aprovação
- **Vantagem:** 8.0 pontos percentuais a favor do App A

#### 2. Análise dos Intervalos de Confiança

##### 90% de Confiança
- **App A:** [83.6%, 92.4%]
- **App B:** [74.6%, 85.4%]
- **Sobreposição:** Mínima (83.6% vs 85.4%)

##### 95% de Confiança
- **App A:** [82.8%, 93.2%]
- **App B:** [73.6%, 86.4%]
- **Sobreposição:** Pequena mas presente

##### 99% de Confiança
- **App A:** [81.2%, 94.8%]
- **App B:** [71.6%, 88.4%]
- **Sobreposição:** Mais significativa

---

## Classificação da Aprovação

### Escala de Satisfação

| Faixa de Aprovação | Classificação | App A | App B |
|-------------------|---------------|-------|-------|
| **85% - 100%** | **Excelente** | ✅ | ❌ |
| **70% - 84%** | **Boa** | ❌ | ✅ |
| **55% - 69%** | **Regular** | ❌ | ❌ |
| **< 55%** | **Insatisfatória** | ❌ | ❌ |

### Interpretação
- **App A:** Aprovação **EXCELENTE** (88%)
- **App B:** Aprovação **BOA** (80%)
- **Diferença de categoria:** App A está em patamar superior

---

## Análise Estatística da Diferença

### Teste Z para Diferença de Proporções

#### Hipóteses
- **H₀:** p₁ = p₂ (proporções iguais)
- **H₁:** p₁ ≠ p₂ (proporções diferentes)

#### Cálculos
- **Proporção pooled:** p̂ = (132 + 120)/(150 + 150) = 0.840
- **Erro padrão pooled:** SE = √[0.840 × 0.160 × (1/150 + 1/150)] = 0.0424
- **Estatística Z:** z = (0.880 - 0.800)/0.0424 = 1.887
- **p-valor:** 0.059

#### Interpretação por Nível
- **α = 0.10:** p = 0.059 < 0.10 → **SIGNIFICATIVO**
- **α = 0.05:** p = 0.059 > 0.05 → **NÃO SIGNIFICATIVO**
- **α = 0.01:** p = 0.059 > 0.01 → **NÃO SIGNIFICATIVO**

---

## Justificativa da Maior Aceitação

### 1. Evidência Numérica
- **Diferença absoluta:** 8 pontos percentuais
- **Diferença relativa:** 10% maior aprovação (88% vs 80%)
- **Consistência:** App A supera App B em todos os cenários

### 2. Significância Estatística
- **90% de confiança:** Diferença é **estatisticamente significativa**
- **95% de confiança:** Diferença é **marginalmente significativa** (p = 0.059)
- **Evidência moderada** de superioridade do App A

### 3. Relevância Prática
- **8 pontos percentuais** é uma diferença **substancial** em pesquisas de satisfação
- **Mudança de categoria:** Excelente vs Boa
- **Impacto na reputação:** Diferença perceptível pelo mercado

### 4. Correlação com Outras Métricas
- **Maior aprovação** correlaciona com **maior consistência** (CV menor)
- **Padrão coerente:** Serviço mais previsível → Maior satisfação
- **Validação cruzada:** Múltiplas métricas apontam para App A

---

## Análise de Confiabilidade

### Tamanho da Amostra
- **n = 150 por grupo** é **adequado** para proporções
- **Margem de erro < 6%** em 95% de confiança
- **Precisão suficiente** para decisões práticas

### Pressupostos Atendidos
- **np ≥ 5 e n(1-p) ≥ 5** para ambos os apps ✅
- **Amostragem aleatória** ✅
- **Independência** das observações ✅

---

## Implicações Estratégicas

### Para o Gestor Público

#### Vantagem do App A
- **Aprovação superior** em 8 pontos percentuais
- **Categoria excelente** vs boa
- **Menor risco reputacional**

#### Considerações
- **Diferença moderada:** Não é uma vantagem esmagadora
- **Significância marginal:** Evidência não é conclusiva a 95%
- **Contexto importante:** Considerar junto com outras métricas

### Para a Decisão Final
- **App A é preferido** pelos usuários
- **Vantagem é consistente** com maior previsibilidade
- **Recomendação:** Considerar aprovação junto com eficiência operacional

---

## Conclusão

### Respostas às Perguntas

1. **Proporções:** App A = 88.0% ± 5.2%, App B = 80.0% ± 6.4% (IC 95%)
2. **Margens de erro:** App A tem menor margem em todos os níveis
3. **Mais aceito:** **App A** com 8 pontos percentuais de vantagem

### Justificativa Final

O **App A é mais aceito pelo público** baseado em:
- **Evidência quantitativa:** 88% vs 80% de aprovação
- **Significância estatística:** Diferença significativa a 90%
- **Relevância prática:** 8 p.p. é diferença substancial
- **Consistência:** Correlaciona com maior previsibilidade do serviço
- **Classificação:** Excelente vs Boa aprovação

A **maior aceitação do App A** reflete a preferência dos usuários por **serviços mais previsíveis e consistentes**, mesmo que ligeiramente mais lentos na média.
