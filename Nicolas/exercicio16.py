def leiaInt(input_texto : str) -> int:
    while True:
        try:
            valor = int(input(input_texto));
            return valor;
        except ValueError:
            print("Valor não é um inteiro")

n = leiaInt("Digite um n: ")
print(n);