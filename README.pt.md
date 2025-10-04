# Projeto de Inteligência Analítica 

## 1. Business Understanding
#### Contexto do Negócio: Este projeto analisa dados reais de um e-commerce de suplementos nutricionais voltado ao consumidor final (B2C), com foco em saúde e bem-estar. O objetivo é entender o comportamento de vendas ao longo de 12 meses e propor soluções analíticas para apoiar decisões comerciais.

#### Objetivo Geral: Realizar uma análise exploratória e preditiva sobre o desempenho comercial, com foco em sazonalidade, eficiência operacional e variáveis que influenciam diretamente o faturamento.

#### Objetivos Específicos:
- Identificar padrões sazonais e variações mensais
- Avaliar métricas operacionais como conversão, ticket médio e receita por visita
- Testar abordagens preditivas para projeção de vendas
- Gerar recomendações estratégicas com base em evidências analíticas
- Diagnosticar variáveis com maior impacto no desempenho comercial

## 2. Data Understanding
#### Fonte dos Dados: Plataforma Mercado Livre Período Analisado: Outubro/2024 a Setembro/2025 
#### Registros: 12 meses completos (Outubro/2025 excluído por inconsistência) 
#### Principais Métricas:
- Visitas
- Compradores únicos
- Conversão (%)
- Quantidade de vendas
- Unidades vendidas
- Vendas brutas
- Ticket médio
= Preço médio por unidade

## 3. Data Preparation
- ETL inicial realizado via Power Query para limpeza estrutural
- Conversão de dados no Python (tratamento de separadores decimais e tipos numéricos)
- Criação de variáveis auxiliares: número do mês, médias móveis, variação percentual
- Ordenação cronológica e validação cruzada com os dados originais

## 4. Modeling
#### Modelo 1 — Machine Learning (Random Forest Regressor)
##### Configuração:
 - Treinamento: 9 meses
 - Teste: 3 meses

##### Variáveis utilizadas: visitas, compradores, conversão, ticket médio, entre outras

##### Resultados:
 - MAE: R$ 1.803,76
 - MAPE: 42,2%
 - R²: -2,46
 - Previsões até 50% abaixo do valor real

##### Diagnóstico: O modelo não é recomendado para uso imediato devido à baixa performance e à limitação de dados. A sazonalidade extrema e o volume reduzido 
(12 pontos temporais) dificultam a generalização.

##### Variáveis mais relevantes identificadas:
 - Compradores únicos
 - Quantidade de vendas
 - Visitas
 - Valor médio por venda

## 5. Modeling Alternativo
#### Modelo 2 — Médias Móveis + Fatores Sazonais
##### Abordagem:
 - Cálculo de médias móveis de 3 e 6 meses
 - Identificação de fatores sazonais por mês
 - Ajuste de previsões com base em tendência e sazonalidade
 - Sistema de Alertas:

🔴 Vendas abaixo da média (>20%)

🟢 Vendas acima da média (>20%)

🟡 Vendas dentro da expectativa

##### Previsões para Outubro-Dezembro:
 - Outubro: R$ 3.800
 - Novembro: R$ 3.200
 - Dezembro: R$ 4.500

## 6. Evaluation
##### Comparativo entre abordagens:
----------------------------------------------------------------------------------------
| Modelo                       |     MAE    |  	MAPE  |  	R²     |  	Recomendação      |
----------------------------------------------------------------------------------------
| Machine Learning (RF)	       |  R$ 1.803  | 	42,2%	 | -2,46	   |  ❌ Não recomendado |
----------------------------------------------------------------------------------------
| Médias Móveis + Sazonalidade	|      —     |   	—	   |    —	    |  ✅ Recomendado     |
----------------------------------------------------------------------------------------

## 7. Deployment
##### Plano de Ação Operacional:
- Reforçar estoque nos meses de alta sazonalidade
- Criar campanhas de reativação nos meses críticos
- Monitorar mensalmente com alertas automáticos
- Revisar trimestralmente com novos dados

##### Metas Realistas para 2025:
- Faturamento anual: R$ 40.000 – R$ 45.000
- Ticket médio: R$ 220
- Conversão: 0,75%

## 8. Next Steps
- Implementar modelo prático no planejamento comercial
- Criar dashboard com métricas-chave
- Coletar dados mensalmente para robustez preditiva
- Reavaliar modelo de ML com 24+ meses de dados
- Desenvolver sistema de recomendações com base em comportamento de compra

## Conclusão
- A análise revelou que o negócio apresenta forte potencial de crescimento, com um faturamento anual de R$ 32.835 e uma evolução de +194,4% ao longo de 12 meses. No entanto, esse crescimento é acompanhado por uma sazonalidade acentuada, com variações mensais superiores a 300%, o que exige planejamento operacional mais preciso.

- Os meses de maior desempenho (Setembro, Julho e Dezembro) concentram picos de vendas que devem ser antecipados com reforço de estoque, campanhas promocionais e equipe preparada. Por outro lado, meses críticos como Abril e Fevereiro demandam estratégias de retenção, reativação de clientes e foco em ticket médio para mitigar quedas.

- A tentativa de aplicar Machine Learning mostrou que, com apenas 12 pontos temporais, o modelo não é confiável para projeções. Em contrapartida, o uso de médias móveis e fatores sazonais se mostrou mais eficaz para gerar previsões realistas e orientar metas trimestrais.

- O negócio deve priorizar o aumento da base de compradores únicos, otimizar a taxa de conversão e elevar o ticket médio — variáveis que demonstraram maior impacto no faturamento. Com a implementação de um sistema de monitoramento contínuo e coleta de dados estruturada, será possível evoluir para modelos preditivos mais robustos e estratégias de recomendação personalizadas.
 
