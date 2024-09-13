import json
with open('dados.json', 'r') as file:
    data = json.load(file)

valores = [item['valor'] for item in data['faturamento'] if item['valor'] > 0]

if not valores:
    print("não há faturamento para calcular.")
else:
    menor_valor = min(valores)
    maior_valor = max(valores)
    media_mensal = sum(valores) / len(valores)
    
    dias_acima_media = sum(1 for valor in valores if valor > media_mensal)
    
    print(f"menor valor de faturamento: {menor_valor}")
    print(f"maior valor de faturamento: {maior_valor}")
    print(f"número de dias com faturamento acima da média: {dias_acima_media}")
