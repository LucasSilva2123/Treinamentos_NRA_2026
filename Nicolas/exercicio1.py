VALOR_DIA = 60.0;
VALOR_KM = 0.15;

while True:
    try:
        dias : int = int(input("Quantos dias o carro foi alugado? \n"));
        km : float = float(input("Quantos km foram rodados? \n"));
        break;
    except ValueError:
        print("Input inválido, tente novamente\n");

valor_total = dias * VALOR_DIA + km * VALOR_KM;

print(f"O valor a pagar é R${valor_total : .2f}");
        
