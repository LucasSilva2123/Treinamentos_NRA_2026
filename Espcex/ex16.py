def leiaInt():
    while True:
        try:
            valor = int(input("Digite apenas um valor inteiro: "))
        except ValueError:
            print("Valor inválido, digite novamente um valor inteiro: ")
        else:
            print(f'O valor digitado foi: {valor}')
            break


leiaInt()