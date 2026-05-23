primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))
total = 0
mais = 10
cont = 0
while mais!=0:
    total += mais
    while cont<total:
        print(primeiro, end = " ")
        primeiro += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Gostaria de adicionar quantos termos? "))
print("Progressão finalizada com {} termos".format(total))
