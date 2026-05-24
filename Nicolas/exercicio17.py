from random import random

tupla : tuple = (
    random(),
    random(),
    random(),
    random(),
    random(),
)

print("Valores: (")
for i in range(5):
    print(f"{tupla[i] : .2f}");

print(")");

print(f"Maior = {max(tupla) : .2f}");
print(f"Menor = {min(tupla) : .2f}")
