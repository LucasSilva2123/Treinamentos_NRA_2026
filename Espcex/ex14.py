def palindromo(frase):
    frase = frase.strip().lower().replace(" ","")
    frase_invertida = frase[::-1]
    if frase == frase_invertida:
        print("A frase é um palíndromo.")
    else:
        print("A frase não é um palíndromo.")


frase = str(input("Digite uma frase: "))
palindromo(frase)