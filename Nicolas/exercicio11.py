while True:
    try:
        valor = int(input("Valor = "));
        break;
    except ValueError:
        print("Input inválido, tente novamente");

cedulas_50 : int = 0;
cedulas_20 : int = 0;
cedulas_10 : int = 0;
cedulas_1 : int = 0;

while valor > 0:
    if valor - 50 >= 0:
        valor -= 50
        cedulas_50 += 1;

    elif valor - 20 >= 0:
        valor -= 20;
        cedulas_20 += 1;

    elif valor - 10 >= 0:
        valor -= 10;
        cedulas_10 += 1;

    elif valor - 1 >= 0:
        valor -= 1;
        cedulas_1 += 1;

print("Será preciso:")
print(f"{cedulas_50} notas de 50");
print(f"{cedulas_20} notas de 20");
print(f"{cedulas_10} notas de 10");
print(f"{cedulas_1} notas de 1");
