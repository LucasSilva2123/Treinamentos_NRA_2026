while True:
    try:
        n_valores = int(input("Quantos valores?\n"))
        break;
    except ValueError:
        print("Input inválido, tente novamente");

valores : list = []
for i in range(n_valores):
    while True:
        try:
            valor = int(input(f"{i} = "))
            break;
        except ValueError:
            print("Input inválido, tente novamente");

    valores.append(valor);

valores_pares : list = [];
valores_impares : list = [];

for valor in valores:
    if valor % 2 == 0:
        valores_pares.append(valor);
    else:
        valores_impares.append(valor);

print(f"Valores = {valores}");
print(f"Valores pares = {valores_pares}");
print(f"Valores impares = {valores_impares}")