largura = float(input("Digite a largura da parede em metros:"))
altura = float(input("Digite a altura da parede em metros:"))
area = largura*altura
tinta = area/2
print("A área da parede é de: {:.2f} m²".format(area))
print("A quantidade de litros de tinta é de: {:.2f} L".format(tinta))