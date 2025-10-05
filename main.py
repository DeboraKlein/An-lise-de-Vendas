# main.py - Script principal de execução

from analise_essencia_vital import AnalisadorEssenciaVital

def main():
    # Inicializar o analisador
    analisador = AnalisadorEssenciaVital('evolucao2425.csv')
    
    # Executar análise completa
    resultados = analisador.executar_analise_completa()
    
    # Acessar e mostrar resultados específicos
    print("\n" + "="*50)
    print("RESULTADOS PRINCIPAIS")
    print("="*50)
    
    metricas = resultados['metricas']
    sazonalidade = resultados['sazonalidade']
    previsoes = resultados['previsoes']
    
    print(f"📊 Faturamento Total: R$ {metricas['vendas_total']:,.0f}")
    print(f"📈 Crescimento Anual: {metricas['crescimento_anual']:+.1f}%")
    print(f"👥 Taxa de Conversão: {metricas['taxa_conversao_media']:.2f}%")
    print(f"💰 Ticket Médio: R$ {metricas['ticket_medio']:.2f}")
    
    print(f"\n🎭 SAZONALIDADE:")
    print(f"• Pico: {sazonalidade['pico_mes']} - R$ {sazonalidade['pico_valor']:,.0f}")
    print(f"• Vale: {sazonalidade['vale_mes']} - R$ {sazonalidade['vale_valor']:,.0f}")
    print(f"• Variação: {sazonalidade['variacao_maxima']:.1f}%")
    
    print(f"\n🔮 PREVISÕES:")
    for mes, valor in previsoes.items():
        print(f"• {mes}: R$ {valor:,.0f}")
    
    # Resultados do Machine Learning
    ml_results = resultados['resultados_ml']
    print(f"\n🤖 MODELO PREDITIVO:")
    print(f"• MAPE: {ml_results['mape']:.1f}%")
    print(f"• R²: {ml_results['r2']:.2f}")
    
    print(f"\n🎯 VARIÁVEIS MAIS IMPORTANTES:")
    for _, row in ml_results['importancia_variaveis'].head(3).iterrows():
        print(f"• {row['feature']}: {row['importance']:.1%}")

if __name__ == "__main__":
    main()