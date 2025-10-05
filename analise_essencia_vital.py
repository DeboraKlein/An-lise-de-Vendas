# analise_essencia_vital.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
from sklearn.ensemble import RandomForestRegressor  
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error

warnings.filterwarnings('ignore')

class AnalisadorEssenciaVital:
    def __init__(self, arquivo_dados):
        self.arquivo_dados = arquivo_dados
        self.df = None
        self.dados_ordenados = None
        
    def carregar_dados(self):
        """Carrega e corrige a estrutura dos dados"""
        with open(self.arquivo_dados, 'r', encoding='utf-8-sig') as f:
            linhas = f.readlines()
        
        cabecalho = linhas[0].strip().replace('"', '').split(';')
        
        dados = []
        for linha in linhas[1:]:
            linha_limpa = linha.strip().replace('"', '')
            valores = linha_limpa.split(';')
            dados.append(valores)
        
        self.df = pd.DataFrame(dados, columns=cabecalho)
        
        # Converter colunas numéricas
        colunas_numericas = ['Visitas', 'Compradores_unicos', 'Media_de_venda_ por_comprador', 
                            'Novos_compradores', 'Quantidade_de_vendas', 'Unidades_vendidas', 
                            'Vendas_brutas', 'Conversao', 'Valor_medio_por_venda', 'Preco_medio_por_unidade']
        
        for coluna in colunas_numericas:
            self.df[coluna] = self.df[coluna].str.replace(',', '.').astype(float)
        
        # Ordenar por ordem cronológica
        ordem_meses = ['Outubro', 'Novembro', 'Dezembro', 'Janeiro', 'Fevereiro', 'Março', 
                      'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro']
        mes_para_numero = {mes: i+1 for i, mes in enumerate(ordem_meses)}
        self.df['mes_num'] = self.df['Mes'].map(mes_para_numero)
        self.dados_ordenados = self.df.sort_values('mes_num').reset_index(drop=True)
        
        return self.df
    
    def calcular_metricas_principais(self):
        """Calcula métricas principais do negócio"""
        visitas_total = self.df['Visitas'].sum()
        vendas_total = self.df['Vendas_brutas'].sum()
        compradores_total = self.df['Compradores_unicos'].sum()
        
        metricas = {
            'visitas_total': visitas_total,
            'vendas_total': vendas_total,
            'compradores_total': compradores_total,
            'media_mensal_vendas': self.df['Vendas_brutas'].mean(),
            'taxa_conversao_media': (compradores_total / visitas_total * 100),
            'ticket_medio': self.df['Valor_medio_por_venda'].mean(),
            'crescimento_anual': ((self.dados_ordenados['Vendas_brutas'].iloc[-1] - 
                                 self.dados_ordenados['Vendas_brutas'].iloc[0]) / 
                                self.dados_ordenados['Vendas_brutas'].iloc[0] * 100)
        }
        
        return metricas
    
    def analisar_sazonalidade(self):
        """Analisa padrões sazonais nos dados"""
        dados = self.dados_ordenados.copy()
        dados['variacao_vendas'] = dados['Vendas_brutas'].pct_change() * 100
        
        # Identificar picos e vales
        pico = dados.loc[dados['Vendas_brutas'].idxmax()]
        vale = dados.loc[dados['Vendas_brutas'].idxmin()]
        
        # Calcular fatores sazonais
        fatores_sazonais = {}
        for mes_num in range(1, 13):
            meses_correspondentes = dados[dados['mes_num'] == mes_num]
            if len(meses_correspondentes) > 0:
                mes_nome = meses_correspondentes['Mes'].iloc[0]
                media_mes = meses_correspondentes['Vendas_brutas'].mean()
                fator_sazonal = media_mes / dados['Vendas_brutas'].mean()
                fatores_sazonais[mes_nome] = fator_sazonal
        
        sazonalidade = {
            'pico_mes': pico['Mes'],
            'pico_valor': pico['Vendas_brutas'],
            'vale_mes': vale['Mes'],
            'vale_valor': vale['Vendas_brutas'],
            'variacao_maxima': ((pico['Vendas_brutas'] - vale['Vendas_brutas']) / vale['Vendas_brutas'] * 100),
            'fatores_sazonais': fatores_sazonais,
            'variacoes_mensais': dict(zip(dados['Mes'], dados['variacao_vendas']))
        }
        
        return sazonalidade
    
    def executar_modelo_preditivo(self):
        """Executa modelo de machine learning para previsões"""
        features = ['mes_num', 'Visitas', 'Compradores_unicos', 'Quantidade_de_vendas', 
                   'Unidades_vendidas', 'Conversao', 'Valor_medio_por_venda']
        target = 'Vendas_brutas'
        
        features_disponiveis = [f for f in features if f in self.dados_ordenados.columns]
        X = self.dados_ordenados[features_disponiveis].fillna(0)
        y = self.dados_ordenados[target].fillna(0)
        
        # Split temporal
        X_treino, X_teste = X.iloc[:9], X.iloc[9:]
        y_treino, y_teste = y.iloc[:9], y.iloc[9:]
        
        modelo = RandomForestRegressor(n_estimators=100, random_state=42, max_depth=5)
        modelo.fit(X_treino, y_treino)
        
        y_pred = modelo.predict(X_teste)
        
        # Métricas
        mae = mean_absolute_error(y_teste, y_pred)
        mape = mean_absolute_percentage_error(y_teste, y_pred) * 100
        r2 = modelo.score(X_teste, y_teste)
        
        # Importância das variáveis
        importancia = pd.DataFrame({
            'feature': features_disponiveis,
            'importance': modelo.feature_importances_
        }).sort_values('importance', ascending=False)
        
        resultados = {
            'mae': mae,
            'mape': mape,
            'r2': r2,
            'importancia_variaveis': importancia,
            'previsoes_teste': y_pred,
            'reais_teste': y_teste.values
        }
        
        return resultados
    
    def gerar_previsoes_praticas(self, sazonalidade):
        """Gera previsões usando abordagem prática baseada em sazonalidade"""
        base_previsao = self.dados_ordenados['Vendas_brutas'].tail(3).mean()
        crescimento_medio = self.dados_ordenados['Vendas_brutas'].pct_change().mean()
        
        meses_futuros = ['Outubro', 'Novembro', 'Dezembro']
        previsoes = {}
        
        for mes in meses_futuros:
            fator = sazonalidade['fatores_sazonais'].get(mes, 1.0)
            previsao = base_previsao * fator * (1 + crescimento_medio)
            previsoes[mes] = previsao
        
        return previsoes
    
    def salvar_resultados(self, metricas, sazonalidade, previsoes):
        """Salva resultados em arquivos"""
        # Salvar dados corrigidos
        self.df.to_csv('dados_finais_corrigidos.csv', index=False, encoding='utf-8-sig')
        
        # Salvar relatório executivo
        with open('relatorio_executivo.txt', 'w', encoding='utf-8') as f:
            f.write("RELATÓRIO EXECUTIVO - ESSÊNCIA VITAL\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Período Analisado: 12 meses (Out/2024 a Set/2025)\n")
            f.write(f"Faturamento Total: R$ {metricas['vendas_total']:,.0f}\n")
            f.write(f"Crescimento Anual: {metricas['crescimento_anual']:+.1f}%\n")
            f.write(f"Taxa de Conversão: {metricas['taxa_conversao_media']:.2f}%\n\n")
            
            f.write("PRINCIPAIS INSIGHTS:\n")
            f.write(f"- Mês de Pico: {sazonalidade['pico_mes']} (R$ {sazonalidade['pico_valor']:,.0f})\n")
            f.write(f"- Mês de Vale: {sazonalidade['vale_mes']} (R$ {sazonalidade['vale_valor']:,.0f})\n")
            f.write(f"- Variação Máxima: {sazonalidade['variacao_maxima']:.1f}%\n\n")
            
            f.write("PREVISÕES PARA PRÓXIMOS MESES:\n")
            for mes, valor in previsoes.items():
                f.write(f"- {mes}: R$ {valor:,.0f}\n")
    
    def executar_analise_completa(self):
        """Executa toda a análise de forma integrada"""
        print("Iniciando análise da Essência Vital...")
        
        # 1. Carregar dados
        self.carregar_dados()
        print("✓ Dados carregados e processados")
        
        # 2. Calcular métricas
        metricas = self.calcular_metricas_principais()
        print("✓ Métricas calculadas")
        
        # 3. Análise de sazonalidade
        sazonalidade = self.analisar_sazonalidade()
        print("✓ Análise de sazonalidade concluída")
        
        # 4. Modelo preditivo
        resultados_ml = self.executar_modelo_preditivo()
        print("✓ Modelo preditivo executado")
        
        # 5. Previsões práticas
        previsoes = self.gerar_previsoes_praticas(sazonalidade)
        print("✓ Previsões geradas")
        
        # 6. Salvar resultados
        self.salvar_resultados(metricas, sazonalidade, previsoes)
        print("✓ Resultados salvos")
        
        print("\nAnálise concluída com sucesso!")
        
        return {
            'metricas': metricas,
            'sazonalidade': sazonalidade,
            'resultados_ml': resultados_ml,
            'previsoes': previsoes
        }

# Execução principal
if __name__ == "__main__":
    analisador = AnalisadorEssenciaVital('evolucao2425.csv')
    resultados = analisador.executar_analise_completa()