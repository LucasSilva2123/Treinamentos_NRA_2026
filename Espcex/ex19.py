lista1 = list()
lista2 = list()
lista3 = list()
while True:
    lista1.append(int(input("Digite um valor: ")))
    continuar = str(input("Deseja continuar[S/N]? ")).strip().upper()
    if continuar == 'N':
        break
for n in lista1:
    if n % 2 == 0:
        lista2.append(n)
    else:
        lista3.append(n)
print(f'Você digitou os valores: {lista1}')
print(f'Os valores pares são: {lista2}')
print(f'Os valores ímpares são: {lista3}')