soma = 0
for c in range(1,7,1):
    n = int(input("Digite o numero {}: ".format(c)))
    if n % 2 == 0:
        soma += n
print("A soma dos  números pares é : {}".format(soma))