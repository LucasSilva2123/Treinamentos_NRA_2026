numeros = list()
for n in range(0,5):
    numeros.append(int(input("Digite um valor: ")))
print(numeros)
print(f'O maior valor é: {max(numeros)}, e a sua posição é: {numeros.index(max(numeros))}')
print(f'O menor valor é: {min(numeros)}, e a sua posição é: {numeros.index(min(numeros))}')
