import random

numeros = tuple(random.randint(1, 100) for n in range(5))
print(numeros)
print(f'O maior valor é {max(numeros)}')
print(f'O menor valor é {min(numeros)}')