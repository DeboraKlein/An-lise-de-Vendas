# Análise Preditiva e de Sazonalidade - Loja online que vende em Marketplaces (Mercado Livre)

## Visão Geral do Projeto
Este projeto realiza análise de sazonalidade e preditiva para a Essência Vital Suplementos, empresa do segmento de suplementos alimentares voltada para o público que busca boa forma física e saúde. Utilizando dados do Mercado Livre, desenvolvi insights estratégicos para otimizar vendas, especialmente durante o período do Projeto Verão.

## Objetivos do Projeto
Objetivo Principal
Identificar padrões sazonais e desenvolver modelo preditivo para otimizar estratégias de vendas durante o período do Projeto Verão.

## Objetivos Específicos
Analisar sazonalidade das vendas ao longo de 9 meses

Desenvolver modelo preditivo para vendas futuras

Identificar oportunidades específicas para suplementos alimentares

Fornecer insights para campanhas do Projeto Verão

## Dados Analisados
### Fonte dos Dados
- Mercado Livre (período: Janeiro a Setembro)

- 9 meses completos de dados transacionais

### Métricas Principais
- Visitas à loja

- Vendas brutas

- Compradores únicos

- Quantidade de vendas

- Unidades vendidas

- Taxa de conversão

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
#### Coleta e Exploração
python
- Carregamento e exploração inicial
````
evolucao = pd.read_csv("Relatorio_evolucao_negocio_2025_01_01-2025_10_01.csv")
print(f"Shape inicial: {evolucao.shape}")
print(f"Colunas disponíveis: {evolucao.columns.tolist()}")
````
#### Desafios Identificados
- Dados inconsistentes (Outubro com valores incorretos)

- Problemas de encoding e formatação

- Valores multiplicados por 10 em algumas colunas

- Necessidade de tratamento de acentos

### 3. Data Preparation
#### Limpeza e Transformação
python
Correção de valores problemáticos
````
evolucao_limpa.loc[evolucao_limpa['Mês'] == 'Agosto', 'visitas'] = 2570
evolucao_limpa.loc[evolucao_limpa['Mês'] == 'Outubro', 'visitas'] = 210

# Padronização de nomes de colunas
mapeamento_colunas = {
    'mes': ['mês', 'mes', 'month'],
    'visitas': ['visita', 'visit', 'access'],
    # ... demais mapeamentos
}
````
#### Processos Realizados
- Exclusão do mês de Outubro (dados inconsistentes)

- Correção de valores multiplicados por 10

- Padronização de nomes de meses

- Tratamento de valores missing

- Criação de variáveis numéricas para meses

### 4. Modeling
#### Modelo Preditivo
python
Features selecionadas
````
features = ['mes_num', 'visitas', 'compradores_unicos', 'quantidade_vendas']
target = 'vendas_brutas'
````

Treinamento do modelo
````
modelo = RandomForestRegressor(n_estimators=100, random_state=42, max_depth=4)
modelo.fit(X_treino, y_treino)
````
#### Abordagem de Validação
- Split temporal: 7 meses treino / 2 meses teste

- Métricas: MAE, MAPE, R²

- Análise de importância de variáveis

### 5. Evaluation
#### Desempenho do Modelo
- MAE: R$ [valor]

- MAPE: 38.1%

- R²: -2.96 (modelo necessita de melhorias)

#### Insights Críticos
- Dados muito voláteis para modelo complexo

- Necessidade de mais dados históricos

- R² negativo indica que média simples seria melhor

- Foco em análise sazonal mais valioso que previsões numéricas

### 6. Deployment
#### Insights Implementáveis
##### Estratégias Projeto Verão:

- Antecipar campanhas para Junho

- Foco em produtos termogênicos e queimadores

- Campanhas progressivas: "Desafio 90 dias"

- Gestão de estoque antecipada

##### Recomendações de Ação
- Maio: Planejamento das campanhas

- Junho: Lançamento do "Desafio Verão"

- Julho: Campanhas de resultados parciais

- Agosto: Foco em "última chance"

- Setembro: Transição para manutenção

## Principais Resultados
### Análise de Sazonalidade
- Melhor mês: Julho (R$ 4.539)

- Pior mês: Fevereiro (R$ 248)

- Crescimento médio: [valor]%

- Padrão identificado: Forte sazonalidade no pré-verão

#### Insights para Suplementos
python
````
produtos_verao = {
    "Termogênicos": "Aumentam metabolismo para queima de gordura",
    "Whey Protein": "Manutenção muscular durante cortes",
    "BCAA": "Preservação muscular em dietas",
    "Queimadores": "Aceleradores de metabolismo",
}
````
### Estratégias Recomendadas
- Pré-Verão (Junho-Julho): Campanhas agressivas

- Verão (Agosto-Setembro): Manutenção de resultados

- Pós-Verão: Fidelização de clientes conquistados

## Próximos Passos
### Melhorias Técnicas
- Coleta de mais dados históricos

- Desenvolvimento de modelo mais simples

- Incorporação de variáveis externas (feriados, clima)

- Análise de cohort para entender comportamento de clientes

### Ações de Negócio
- Implementar campanhas do Projeto Verão

- Monitorar resultados em tempo real

- Ajustar estratégias baseado em performance

- Expandir análise para outros períodos sazonais

## Estrutura de Arquivos

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
- Analista de Dados - Debora Rebula Klein
- Domínio do Negócio - Equipe Essência Vital Suplementos

## Contato
Para mais informações sobre esta análise, entre em contato com 

Data da última atualização: 03/10/2025
 
