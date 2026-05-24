frase = input("Insira a frase \n")

frase_normalizada = frase.lower();

print(f"A letra 'A' aparece {frase_normalizada.count("a")}");
print(f"A letra 'A' aparece pela primeira vez na posição {frase_normalizada.find("a")}")
print(f"A letra 'A' aparece pela ultima vez na posição {frase_normalizada.rfind("a")}")