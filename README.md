# Case de Inteligência Comercial | Análise de Vendas 2025
#### Este projeto analisa dados de vendas e comportamento de compradores ao longo de 2025. Utilizamos Python e Jupyter para ETL, análise exploratória, simulação de metas e exportação dos dados tratados para visualização em Power BI.

##  1. Entendimento do Negócio
O objetivo é entender a evolução do negócio, identificar padrões de compra, avaliar desempenho de produtos e publicações, e simular estratégias para alcançar uma meta de crescimento de +15% na receita.

### Principais perguntas:

- Como evoluíram as vendas ao longo do ano?

- Quais faixas de preço e tipos de compradores convertem melhor?

- Quais produtos têm maior intenção de compra?

- Quais anúncios geram mais impacto?

- Quais estratégias podem impulsionar o crescimento?

## 2. Entendimento dos Dados
### Fontes utilizadas:

- Relatorio_evolucao_negocio_2025_01_01-2025_10_01.csv

- vendas_por_faixa_preco_2025.csv

- vendas_por_tipo_comprador_2025.csv

- Relatorio_desempenho_do_produt_2025.csv

- Relatorio_desempenho_publicacoes_2025.csv

### Principais colunas tratadas:

Datas, valores brutos, taxas de conversão, intenção de compra, visitas únicas, cancelamentos, devoluções, etc.

## 3. Preparação dos Dados
- Padronização de nomes de colunas

- Remoção de colunas Unnamed

- Conversão de datas e percentuais (com vírgula e %)

- Tratamento de nulos e tipos numéricos

- Criação de colunas derivadas como gap_intencao_venda e potencial

- Todos os dados tratados foram exportados para a pasta dados_tratados/.

##  4. Modelagem
### A modelagem foi orientada por roteiro analítico dividido em 6 blocos:

- Evolução Mensal do Negócio Receita, conversão, recompra, cancelamentos e devoluções

- Vendas por Faixa de Preço Receita, conversão, perfil de compradores

- Vendas por Tipo de Comprador Participação, conversão, novos vs. recorrentes

- Desempenho por Produto Intenção vs. vendas reais, conversão, receita

- Desempenho por Publicação Impacto, conversão, participação na receita

- Simulação de Meta (+15%) Produtos e faixas com maior potencial de crescimento

## 5. Avaliação
### Principais insights:

A conversão média por faixa de preço varia fortemente entre segmentos

Produtos com alta intenção nem sempre convertem bem

Publicações com maior impacto nem sempre têm maior conversão

Tipo de comprador recorrente tem maior participação na receita

A meta de +15% é viável com foco em produtos de alta intenção e faixas com boa conversão

##  6. Implantação
Os dados tratados foram exportados para CSV e estão prontos para uso em Power BI. A estrutura do repositório é:

   dados_tratados/
   
├── evolucao_negocio.csv

├── faixa_preco.csv

├── tipo_comprador.csv

├── desempenho_produto.csv

├── desempenho_publicacoes.csv

├── simulacao_meta_15.csv

   scripts/
   
├── ProjetoSazionalidadeTendencias

   docs/
   
├── apresentacao.pptx

├── glossario.csv
