casa=float(input("Digite o valor da casa:"))
salário=float(input("Digite o seu salário:"))
tempo=int(input("Digite em quantos anos irá pagar:"))
prestaçao_mensal=casa/(tempo*12)
if(prestaçao_mensal<0.3*salário):
    print("Empréstimo será concedido")
else:
    print("Empréstimo negado")