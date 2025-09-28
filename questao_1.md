# QUESTÃO 1 - Estimativa do Tempo Médio de Espera

**Disciplina:** Inferência Estatística I - UFPB CCEN  
**Aluno:** Diogo Da Silva Rego (20240045381)  
**Professora:** Tatiene Correia  
**Tema II:** Transporte Urbano (Comparação entre aplicativos)

---

## Pergunta
**Qual é a estimativa do tempo médio de espera de cada aplicativo? Qual a margem de erro e a amplitude associadas às estimativas em diferentes níveis de confiança (90%, 95% e 99%)? Interprete os resultados.**

---

## Dados Utilizados
- **App A:** n₁ = 35 observações
- **App B:** n₂ = 55 observações
- **Total:** 90 observações de tempo de espera (em minutos)

---

## Cálculos dos Intervalos de Confiança

### Aplicativo A

| Nível de Confiança | Média | Margem de Erro | Amplitude | Limite Inferior | Limite Superior |
|-------------------|-------|----------------|-----------|-----------------|-----------------|
| **90%** | 7.434 min | 0.306 min | 0.612 min | 7.128 min | 7.740 min |
| **95%** | 7.434 min | 0.368 min | 0.736 min | 7.066 min | 7.802 min |
| **99%** | 7.434 min | 0.494 min | 0.988 min | 6.940 min | 7.928 min |

**Fórmula utilizada:** IC(μ; 1-α) = x̄ ± t(α/2; n-1) × (s/√n)

**Estatísticas descritivas App A:**
- Média: 7.434 min
- Desvio padrão: 1.071 min
- Erro padrão: 0.181 min

### Aplicativo B

| Nível de Confiança | Média | Margem de Erro | Amplitude | Limite Inferior | Limite Superior |
|-------------------|-------|----------------|-----------|-----------------|-----------------|
| **90%** | 6.811 min | 0.351 min | 0.702 min | 6.460 min | 7.162 min |
| **95%** | 6.811 min | 0.421 min | 0.842 min | 6.390 min | 7.232 min |
| **99%** | 6.811 min | 0.560 min | 1.121 min | 6.251 min | 7.372 min |

**Estatísticas descritivas App B:**
- Média: 6.811 min
- Desvio padrão: 1.556 min
- Erro padrão: 0.210 min

---

## Interpretação dos Resultados

### 1. Comparação das Médias
- **App B é mais rápido:** Tempo médio de 6.81 min vs 7.43 min do App A
- **Diferença:** 0.62 minutos (37 segundos) a favor do App B

### 2. Precisão das Estimativas
- **App A tem maior precisão:** Margens de erro menores em todos os níveis
- **App B tem maior incerteza:** Margens de erro 15-20% maiores que o App A
- **Causa:** Maior variabilidade nos dados do App B (DP = 1.556 vs 1.071)

### 3. Comportamento por Nível de Confiança
- **90% → 95%:** Aumento de ~20% na margem de erro
- **95% → 99%:** Aumento de ~35% na margem de erro
- **Trade-off:** Maior confiança = menor precisão (intervalos mais largos)

### 4. Sobreposição dos Intervalos
- **90%:** Sobreposição mínima entre os intervalos
- **95%:** Sobreposição pequena mas presente
- **99%:** Sobreposição mais significativa

### 5. Implicações Práticas
- **App B:** Mais rápido na média, mas com maior variabilidade
- **App A:** Mais lento, mas mais previsível e confiável
- **Decisão:** Depende se a prioridade é velocidade média ou consistência do serviço

---

## Conclusão Estatística

Com **95% de confiança**, podemos afirmar que:
- O tempo médio do **App A** está entre **7.07 e 7.80 minutos**
- O tempo médio do **App B** está entre **6.39 e 7.23 minutos**

A **diferença observada** de 0.62 minutos é **estatisticamente relevante**, mas deve ser considerada junto com a maior variabilidade do App B, que pode impactar a experiência do usuário.
