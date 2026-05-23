dias = int(input("Digite o numero de dias que o carro foi alugado:"))
distancia = float(input("Digite quantos km o carro percorreu:"))
preco = (dias * 60) + (distancia * 0.15)
print("O preço a pagar é de R$ {:.2f}".format(preco))