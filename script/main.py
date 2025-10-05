# main.py - Script principal com caminho absoluto

import os
import sys
from analise_essencia_vital import AnalisadorEssenciaVital

def main():
    print("📍 Verificando ambiente...")
    
    # Caminho absoluto para o arquivo CSV
    caminho_base = r'C:\Users\debor\OneDrive\Github\Previsão de demanda'
    arquivo_csv = os.path.join(caminho_base, 'evolucao2425.csv')
    
    print(f"📁 Diretório base: {caminho_base}")
    print(f"📄 Procurando por: {arquivo_csv}")
    
    # Verificar se o arquivo existe
    if not os.path.exists(arquivo_csv):
        print("❌ ERRO: Arquivo CSV não encontrado!")
        print("📋 Arquivos no diretório:")
        try:
            arquivos = os.listdir(caminho_base)
            for arquivo in arquivos:
                if arquivo.endswith('.csv'):
                    print(f"   ✅ {arquivo}")
                else:
                    print(f"   📄 {arquivo}")
        except Exception as e:
            print(f"   Erro ao listar arquivos: {e}")
        return
    
    print(f"✅ Arquivo encontrado: {arquivo_csv}")
    
    # Inicializar o analisador
    print("🚀 Iniciando análise...")
    analisador = AnalisadorEssenciaVital(arquivo_csv)
    
    try:
        # Executar análise completa
        resultados = analisador.executar_analise_completa()
        
        # Mostrar resultados
        print("\n" + "="*60)
        print("🎉 ANÁLISE CONCLUÍDA - RESULTADOS PRINCIPAIS")
        print("="*60)
        
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
        
        print(f"\n🔮 PREVISÕES PRÓXIMOS MESES:")
        for mes, valor in previsoes.items():
            print(f"• {mes}: R$ {valor:,.0f}")
            
        print(f"\n💾 Arquivos gerados:")
        print("   - dados_finais_corrigidos.csv")
        print("   - relatorio_executivo.txt")
        print("   - relatorio_analise_completa.csv")
        
    except Exception as e:
        print(f"❌ Erro durante a análise: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
