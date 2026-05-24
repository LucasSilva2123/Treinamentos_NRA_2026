from random import random

lista : list = [
    random(),
    random(),
    random(),
    random(),
    random(),
]

print("Valores: [")
for i in range(5):
    print(f"{lista[i] : .2f}");

print("]");

print(f"Maior = {max(lista) : .2f}");
print(f"Menor = {min(lista) : .2f}")
