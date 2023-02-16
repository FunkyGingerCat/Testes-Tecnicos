### Faturamento Diário ###

# valores de faturamento diário
dia1 = 22174.1664  # quarta-feira
dia2 = 24537.6698  # quinta-feira
dia3 = 26139.6134  # sexta-feira
dia4 = 0.0         # sábado
dia5 = 0.0         # domingo
dia6 = 26742.6612  # segunda-feira
dia7 = 0.0         # terça-feira feriado
dia8 = 42889.2258  # quarta-feira
dia9 = 46251.174   # quinta-feira
dia10 = 11191.4722 # sexta-feira
dia11 = 0.0        # sábado
dia12 = 0.0        # domingo
dia13 = 3847.4823  # segunda-feira
dia14 = 373.7838   # terça-feira
dia15 = 2659.7563  # quarta-feira
dia16 = 48924.2448 # quinta-feira
dia17 = 18419.2614 # sexta-feira
dia18 = 0.0        # sábado
dia19 = 0.0        # domingo
dia20 = 35240.1826 # segunda-feira
dia21 = 43829.1667 # terça-feira
dia22 = 18235.6852 # quarta-feira
dia23 = 4355.0662  # quinta-feira
dia24 = 13327.1025 # sexta-feira
dia25 = 0.0        # sábado
dia26 = 0.0        # domingo
dia27 = 25681.8318 # segunda-feira
dia28 = 1718.1221  # terça-feira
dia29 = 13220.495  # quarta-feira
dia30 = 8414.61    # quinta-feira

# listagem dos dias de faturamento
faturamento_diario = [dia1, dia2, dia3, dia4, dia5, dia6, dia7, dia8, dia9, dia10, dia11, dia12, dia13, dia14, dia15, dia16, 
                      dia17, dia18, dia19, dia20, dia21, dia22, dia23, dia24, dia25, dia26, dia27, dia28,dia29, dia30]


# calcula o menor valor de faturamento diário, sem os valores zerados
sem_zeros = [valor for valor in faturamento_diario if valor != 0]
menor_faturamento = min(sem_zeros)

# calcula o maior valor de faturamento diário
maior_faturamento = max(faturamento_diario)

# calcular a média de faturamento diário
media_faturamento = sum(faturamento_diario) / len(faturamento_diario)

# calcula o número de dias em que o valor de faturamento diário foir maior que média mensal
dias_acima_media = len([f for f in faturamento_diario if f > media_faturamento])

# Mostra os resultados
print("*** Faturamento Diário ***")
print(f"O menor valor de faturamento ocorrido no mês foi R$ {menor_faturamento:.2f}")
print(f"O maior valor de faturamento ocorrido no mês foi R$ {maior_faturamento:.2f}")
print(f"Dias no mês em que o valor de faturamento diário foi maior que média: {dias_acima_media} dias")
