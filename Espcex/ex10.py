n = 0
while n >= 0:
    n = int(input("Digite um numero: "))
    if n >= 0:
        for c in range(1,11,1):
            print("{} x {} = {}".format(n,c,n*c))