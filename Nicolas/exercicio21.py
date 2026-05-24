import numpy as np

A = np.random.uniform(0, 9, (3,3));
B = np.random.uniform(0, 9, (3,3));

print(f"Matriz A = \n{A}\n");
print(f"Matriz B = \n{B}\n");

C = A + B;

print(f"Matriz C (A + B) = \n{C}\n");

D = A * B;

print(f"Matriz D (A * B) = \n{D}\n");

E = A @ B;

print(f"Matriz E (A @ B) = \n{C}\n");