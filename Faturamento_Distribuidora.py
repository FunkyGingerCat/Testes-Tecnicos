### Faturamento da Distribuidora ###

# valores de faturamento das distribuidoras por região
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# o total faturado é igual a soma do faturamento de todas as distribuidoras
total_faturamento = sum(faturamento.values())

print("*** Faturamento da Distribuidora ***")
print(f"O total faturado no mês foi R$ {total_faturamento}")
print("Percentual de representação de cada estado dentro do faturamento total mensal:")

# define o primeiro parâmetro de faturamento como "estado" e o segundo como "valor"
for estado, valor in faturamento.items():
    # o percentual é igual ao valor divido pelo total faturado multiplado por 100
    percentual = valor / total_faturamento * 100
    # mostra o estado e seu percentual dentro do valor total faturado
    print(f'{estado}: {percentual:.2f}%')
