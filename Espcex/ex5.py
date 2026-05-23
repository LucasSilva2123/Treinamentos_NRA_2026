reta1=float(input("Digite o valor da primeira reta:"))
reta2=float(input("Digite o valor da segunda reta:"))
reta3=float(input("Digite o valor da terceira reta:"))
if(reta1<reta2+reta3 and reta2+reta3 and reta3<reta1+reta2):
    print("As retas formam um triangulo")
    if(reta1==reta2 and reta2==reta3):
        print("O triangulo é equilátero")
    elif(reta1==reta2 or reta2==reta3 or reta1==reta3):
        print("O triangulo é iscósceles")
    elif(reta1!=reta2 and reta2!=reta3 and reta1!=reta3):
        print("O triangulo é escaleno")
else:
    print("As retas não formam um triangulo")

