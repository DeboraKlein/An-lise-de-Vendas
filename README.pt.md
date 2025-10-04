# Análise Preditiva e de Sazonalidade - Essência Vital Suplementos

## Visão Geral do Projeto
Este projeto realiza análise de sazonalidade e preditiva para a Essência Vital Suplementos, empresa do segmento de suplementos alimentares voltada para o público que busca boa forma física e saúde. Utilizando dados do Mercado Livre de 9 meses (Janeiro a Setembro), desenvolvemos insights estratégicos para otimizar vendas, especialmente durante o período do Projeto Verão.

## Objetivos do Projeto

### Objetivo Principal
Identificar padrões sazonais e desenvolver modelo preditivo para otimizar estratégias de vendas durante o período do Projeto Verão.

### Objetivos Específicos
- Analisar sazonalidade das vendas ao longo de 9 meses
- Desenvolver modelo preditivo para vendas futuras
- Identificar oportunidades específicas para suplementos alimentares
- Fornecer insights para campanhas do Projeto Verão

## Dados Analisados

### Fonte dos Dados
- Fonte: Mercado Livre
- Período: Janeiro a Setembro (9 meses completos)
- Total de registros: 10 → 9 meses (após limpeza)
- Colunas analisadas: 17 métricas de desempenho

### Métricas Principais
- Visitas: 2.100 a 6.669 visitas/mês
- Vendas brutas: R$ 248 a R$ 4.539/mês
- Compradores únicos: 127
- Quantidade de vendas: 131

##  Metodologia CRISP-DM

### 1. Business Understanding

#### Contexto do Negócio
- Empresa: Essência Vital Suplementos
- Segmento: Suplementos alimentares
- Público-alvo: Pessoas que buscam boa forma física e saúde
- Período Crítico: Projeto Verão (Setembro a Dezembro)

#### Objetivos de Negócio
- Otimizar campanhas do Projeto Verão
- Antecipar demanda sazonal
- Melhorar gestão de estoque
- Aumentar eficiência de marketing

### 2. Data Understanding

#### Dados Iniciais
- Dataset original: 10 meses, 17 colunas

#### Problemas identificados:
  - Mês de Outubro com dados inconsistentes (210 visitas vs média de 2.500+)
  - Valores de Fevereiro anomalamente baixos (R$ 248)
  - Problema de encoding com acentos ("março" vs "marco")

#### Estatísticas Descritivas Iniciais

- Vendas totais: R$ 22.820,00
- Média mensal: R$ 2.535,56
- Maior venda: R$ 4.539,00 (Julho)
- Menor venda: R$ 248,00 (Fevereiro)
    
### 3. Data Preparation

#### Processos de Limpeza Realizados
- Exclusão de Outubro: Dados inconsistentes (mês incompleto)
- Correção de Março: Problema de acentuação resolvido
- Tratamento de Valores: Correção de valores multiplicados por 10
- Padronização: Meses em minúsculo, sem acentos

#### Dataset Final
- Período: 9 meses (Janeiro a Setembro)
- Meses válidos: janeiro, fevereiro, marco, abril, maio, junho, julho, agosto, setembro
- Dados limpos: Prontos para análise

### 4. Modeling
#### Configuração do Modelo Preditivo
````
# Features selecionadas
features = ['mes_num', 'visitas', 'compradores_unicos', 'quantidade_vendas']
target = 'vendas_brutas'

# Modelo escolhido
RandomForestRegressor(n_estimators=100, random_state=42, max_depth=4)

# Validação temporal
Treino: 7 meses (Janeiro-Julho)
Teste: 2 meses (Agosto-Setembro)
````
#### Importância das Variáveis
- Visitas: 30.0%
- Número do Mês: 28.0%
- Quantidade de Vendas: 21.6%
- Compradores Únicos: 20.4%

### 5. Evaluation

#### Desempenho do Modelo - Resultados Reais
- MAE (Mean Absolute Error): R$ 1.530,55
- MAPE (Mean Absolute Percentage Error): 38.1%
- R²: -2.96

#### Análise Crítica do Modelo

##### Problemas Identificados:
- R² negativo (-2.96): Modelo performa pior que a média simples
- MAPE 38.1%: Erro muito alto para decisões de negócio
- Previsões infladas: Mês 12 projetado em R$ 52.687 (irreal)
- Dados insuficientes: 9 meses é pouco para modelo complexo

#### Comparativo Previsões vs Realidade:
- Agosto: Real R$ 2.724 | Previsto R$ 2.138 | Erro R$ -586
- Setembro: Real R$ 4.532 | Previsto R$ 2.057 | Erro R$ -2.475

### 6. Deployment

#### Análise de Sazonalidade - Resultados Chave

##### Variação Mensal das Vendas:
• Fevereiro: -92.7% (queda extrema - outlier)
• Março: +1026.6% (recuperação dramática)
• Abril: -60.4%
• Maio: +39.2%
• Junho: +24.5%
• Julho: +136.7% (pico do pré-verão)
• Agosto: -40.0%
• Setembro: +66.4% (início do verão)

##### Padrões Sazonais Identificados:

- Pico Principal: Julho (R$ 4.539) - Pré-verão
- Segundo Pico: Setembro (R$ 4.532) - Início do verão
- Vale Crítico: Fevereiro (R$ 248) - Pós-festas
- Forte Sazonalidade: 2º semestre com performance superior

### Análise Específica - Projeto Verão:
#### Performance Verão vs Pré-Verão:
• Julho (pré-verão): R$ 4.539
• Setembro (verão): R$ 4.532  
• Crescimento Julho→Setembro: -0.2% (estabilidade)

### Estratégias Recomendadas para Suplementos

#### Produtos-Chave para Verão:
- Termogênicos: Aumentam metabolismo para queima de gordura
- Whey Protein: Manutenção muscular durante cortes
- BCAA: Preservação muscular em dietas

#### Cronograma de Campanhas - Projeto Verão 2024/2025:
##### Junho: "Desafio 90 dias para o Verão"
- Foco: Termogênicos e queimadores
- Meta: Alcançar patamar de R$ 4.500+

##### Julho: "Metade do Caminho - Resultados Parciais"
- Foco: Manutenção do pico de vendas
- Aproveitar momentum natural do mês

##### Agosto: "Última Chance - 30 dias para a Praia"
- Foco: Produtos de definição muscular
- Estratégia: Urgência e resultados rápidos

##### Setembro: "Verão Garantido - Manutenção"
- Foco: Fidelização e manutenção de resultados
- Produtos: BCAA e vitaminas

### Insights de Negócio Críticos

#### Oportunidades Identificadas:
- Julho é o melhor mês: R$ 4.539 (investir em pré-verão)
- Agosto tem queda: R$ 2.724 (oportunidade de campanhas)
- Setembro mantém alto: R$ 4.532 (bom sinal para verão)

### Expectativas Realistas - Projeto Verão 2024:
#### Base: Performance de Julho e Setembro 2024
##### Expectativa: R$ 4.535 ±20% (mantendo patamar similar)

## Ações Imediatas Recomendadas:

### Gestão de Estoque:
- Aumentar 50% em Maio para Junho-Agosto
- Foco em termogênicos e queimadores

### Campanhas de Marketing:
- Antecipar para Junho (atualmente em R$ 1.918)
- Criar "Desafio Verão" com metas progressivas

### Monitoramento:
Acompanhar performance vs Julho/Setembro 2024

## Conclusões e Recomendações Finais
### Resumo Executivo
#### Pontos Fortes:
- Sazonalidade clara identificada (pico Julho-Setembro)
- Dados de Setembro indicam boa performance no verão
- Opportunity de crescimento em Agosto

#### Limitações:
- Modelo preditivo não confiável (R² negativo)
- Dados voláteis com outliers extremos
- Período curto para análise (9 meses)

#### Recomendações Prioritárias:

- Foco em Análise Sazonal: Mais valiosa que previsões numéricas
- Meta Realista: Manter patamar de R$ 4.500+ no verão
- Antecipação: Começar campanhas em Junho, não Setembro
- Monitoramento Contínuo: Coletar mais dados para modelos futuros

### Próximos Passos
#### Curto Prazo (1-2 meses):
- Implementar campanhas de Junho
- Ajustar estoque para pré-verão
  
#### Médio Prazo (3-6 meses):
- Coletar mais dados para melhorar modelos
- Desenvolver análise de cohort de clientes
  
#### Longo Prazo (12 meses):
- Modelo preditivo robusto com dados anuais
- Análise de múltiplas sazonalidades

### Estrutura de Arquivos
text
projeto_essencia_vital/
├── dados/
│   ├── Relatorio_evolucao_negocio_2025_01_01-2025_10_01.csv
│   ├── dados_evolucao_processados.csv
│   ├── dados_evolucao_FINAL.csv
│   └── dados_9_meses_CORRIGIDOS.csv
├── notebooks/
│   └── analise_sazonalidade_preditiva.ipynb
├── relatorios/
│   └── README.md
└── requirements.txt

## Tecnologias Utilizadas
- Python 3.x
- Pandas - Manipulação de dados
- Scikit-learn - Modelagem preditiva
- Matplotlib/Seaborn - Visualizações
- Jupyter Notebook - Análise exploratória

## Responsáveis
Analista de Dados - Debora Rebula Klein
Domínio do Negócio - Equipe Essência Vital Suplementos

📞 Contato
Para mais informações sobre esta análise, entre em contato com a equipe de dados da Essência Vital Suplementos.

Data da última atualização: 03/10/2025
 
