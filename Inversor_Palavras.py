### Inverter Strings ###

print("*** Inversor de Palavras ***")

while True:
    palavra = (input("Digite a palavra a ser invertida: "))

    # slice notation para inverter a palavra
    palavra_invertida = palavra[::-1]
    # resultado
    print(palavra_invertida)
