import matplotlib.pyplot as plt
import numpy as np
from random import randint

plt.title("Gráfico muito foda")
plt.xlabel("Formigas (trilhões)")
plt.ylabel("Estrelas de neutrons (bilhões)")

for i in range(30):
    dados_aleatorios_x = np.random.uniform(0, 10, (50, 1))
    dados_aleatorios_y = np.random.uniform(0, 10, (50, 1))
    plt.plot(dados_aleatorios_x, dados_aleatorios_y, color = f"#{randint(0, 0xFFFFFF) :06x}");

plt.legend()
plt.show();