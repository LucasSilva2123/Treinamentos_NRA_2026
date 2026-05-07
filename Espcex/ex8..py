somaidade = 0
mul20 = 0
cont = 0
maioridade = 0
nomevelho = ' '
for c in range(1,5):
    nome = str(input("Digite o nome da pessoa {}: ".format(c))).strip()
    idade = int(input("Digite a idade da pessoa {}: ".format(c)))
    somaidade += idade
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Digite o sexo da pessoa {} [M/F]: ".format(c))).strip().upper()[0]
    print("Nome: {}".format(nome))
    print("Idade:  {}".format(idade))
    print("Sexo: {}".format(sexo))
    if sexo == 'F' and idade < 20:
        mul20 += 1
    if sexo == 'M':
        if c == 1:
            nomehomem = nome
            maioridade = idade
        if idade > maioridade:
            nomehomem = nome
            maioridade = idade
    
media = somaidade/4
print("A média das idade é: {}".format(media))
print("O nome do homem mais velho é: {}".format(nomehomem))
print("O número de mulheres com menos de 20 anos é: {}".format(mul20))
