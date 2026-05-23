def max_lista(lista):
    if len(lista) == 0:
        print("Lista vazia")
    maior = lista[0]
    for n in lista:
        if n > maior:
            maior = n
    print("O maior número da lista é: {} ".format(maior))


números = [int(x) for x in input("Digite uma lista de números separados por um espaço: ").split()]
max_lista(números)