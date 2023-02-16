### Teste de Fibonacci ###

print("*** Teste de números na sequência Fibonacci ***")
while True:

    # define os parâmetros das variáveis iniciais
    penultimo = 0
    ultimo = 1

    # numero a ser conferido
    num = int(input("Digite o número a ser conferido: "))

    # enquanto o último número for menor que o número informado pelo usuário:
    while ultimo < num:
        # o número atual é igual a soma do último e penúltimo número
        atual = penultimo + ultimo
        # para seguir o loop da sequência, o penúltimo número torna-se o último
        penultimo = ultimo
         # e o último torna-se o número atual!
        ultimo = atual

    # conferência do resultado
    if ultimo == num:
        print(f"{num} está na sequência Fibonacci.")
    else:
        print(f"{num} não está na sequência Fibonacci.")
