maiores_de_idade : int = 0;
homens : int = 0;
mulheres_com_mais_de_vinte : int = 0;


while True:
    try:
        idade = int(input("Idade = "));
        sexo = input("Sexo (M/F) = ");
    except ValueError:
        print("Inpout inválido, tente novamente");

    if idade > 18:
        maiores_de_idade += 1;

    if sexo == "M":
        homens += 1;

    if sexo == "F" and idade > 20:
        mulheres_com_mais_de_vinte += 1;

    while True:
        try:
            continuar = input("Continuar? (S/N)\n");

            if continuar == "S" or continuar == "N":
                break;

        except ValueError:
            print("Input inválido, tente novamente");

    if continuar == "N":
        break;

print(f"Maiores de idade = {maiores_de_idade}");
print(f"Homens = {homens}");
print(f"Mulheres com mais de 20 = {mulheres_com_mais_de_vinte}")