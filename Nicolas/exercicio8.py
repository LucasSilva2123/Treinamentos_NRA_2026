n_pessoas : int = 0;
idade_total : int = 0;
homem_mais_velho_idade : int = 0;
homem_mais_velho : str = "";
mulheres_com_menos_de_vinte : int = 0;


while True:
    try:
        nome = input("Nome = ");
        idade = int(input("Idade = "));
        sexo = input("Sexo (M/F) = ");
    except ValueError:
        print("Inpout inválido, tente novamente");

    n_pessoas += 1;

    idade_total += idade;

    if sexo == "M":
        if homem_mais_velho_idade < idade:
            homem_mais_velho = nome;
            homem_mais_velho_idade = idade;

    if sexo == "F" and idade < 20:
        mulheres_com_menos_de_vinte += 1;

    while True:
        try:
            continuar = input("Continuar? (S/N)\n");

            if continuar == "S" or continuar == "N":
                break;

        except ValueError:
            print("Input inválido, tente novamente");

    if continuar == "N":
        break;

print(f"Homem mais velho = {homem_mais_velho}");
print(f"Mulheres com menos de 20 = {mulheres_com_menos_de_vinte}");
print(f"Média das idades = {idade_total / n_pessoas}");
