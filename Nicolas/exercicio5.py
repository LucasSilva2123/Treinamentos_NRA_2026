while True:
    try:
        l1 = float(input("Medida do lado 1: "));
        l2 = float(input("Medida do lado 2: "));
        l3 = float(input("Medida do lado 3: "));
        break;
    except ValueError:
        print("Input inválido, tente novamente");

maior_lado = max(l1, l2, l3);

if maior_lado >= (l1 + l2 + l3 - maior_lado):
    print("Não é possível formar um triângulo.");
else:
    triangulo_tipo : str;

    if l1 == l2 and l2 == l3:
        triangulo_tipo = "equilatero"
    elif l1 == l2 or l2 == l3 or l1 == l3:
        triangulo_tipo = "isoceles"
    else:
        triangulo_tipo = "escaleno"

    print(f"É possível formar um triângulo {triangulo_tipo}.\n");