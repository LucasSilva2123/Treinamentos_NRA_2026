import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-20,20,100)
y = x**3 - x**2 + 10
plt.title('Gráfico da função y = x**3 - x**2 + 10')
plt.xlabel('Eixo das coordenadas x')
plt.ylabel('Eixo das ordenadas y')
plt.plot(x,y)
plt.grid(True)
plt.legend(['y = x**3 - x**2 + 10'])
plt.show()