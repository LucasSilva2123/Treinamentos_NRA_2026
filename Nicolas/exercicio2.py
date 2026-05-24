METRO2_POR_TINTA_LITRO : float = 2;

while True:
    try:
        altura = float(input("Qual a altura da parede em metros?\n"));
        largura = float(input("Qual a largura da parede em metros?\n"));
        break;
    except ValueError:
        print("Input inválido, tente novamente\n");

area_metro2 : float = altura * largura;
tinta_litro : float = area_metro2 / METRO2_POR_TINTA_LITRO;
usar_plural : bool = tinta_litro > 1;

print(f"Será necessário {tinta_litro} litro{'s' if usar_plural else ""} de tinta.");