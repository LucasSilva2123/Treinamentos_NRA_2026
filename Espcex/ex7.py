
adult = hom = mul20 = 0
while True:
    idade = int(input("Digite a idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Digite o sexo[M/F]: ")).strip().upper()[0]
    if idade > 18:
        adult += 1
    if sexo == 'M':
        hom += 1
    if sexo == 'F' and idade <20:
        mul20 +=1
    print("{}".format(idade))
    print("{}".format(sexo))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input("Deseja continuar[S/N]? ")).strip().upper()[0]
    if continuar == 'N':
        break
print("Total de pessoas maiores de 18 anos: {}".format(adult))
print("Total de homens: {}".format(hom))
print("Total de mulheres com menos de 20 anos: {}".format(mul20))