import numpy as np

matrizA = np.random.randint(0,10, (3,3))
matrizB = np.random.randint(0,10, (3,3))
print(f'Matriz A:\n {matrizA}')
print(f'Matriz B:\n {matrizB}')
matrizC = matrizA + matrizB
print(f'Matriz C (A + B):\n {matrizC}')
matrizD = matrizA  * matrizB
print(f'Matrix D (A * B):\n {matrizD}')
matrizE = matrizA @ matrizB
print(f'Matriz E (A @ B):\n {matrizE}')