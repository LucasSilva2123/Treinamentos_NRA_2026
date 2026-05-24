while True:
    try:
        valor_inicial = float(input("Qual o valor inicial da PA?\n"));
        razao = float(input("Qual a razão da PA?\n"));
        break;
    except ValueError:
        print("Input inválido, tente novamente");

valor : float = valor_inicial;
posicao : int = 1;
while True:
    for i in range(10):
        print(f"{posicao}: {valor}");
        valor += razao;
        posicao += 1;

    while True:
        try:
            continuar = input("Continuar? (S/N)\n");

            if continuar == "S" or continuar == "N":
                break;
        except ValueError:
            print("Input inválido, tente novamente");

    if continuar == "N":
        break;


