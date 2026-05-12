import matplotlib.pyplot as plt

edades = [18, 19, 21, 25, 26, 56, 30, 32, 38, 45, 50]

plt.hist(edades, bins=8)
plt.title("Histograma de edades")
plt.xlabel("Edades")
plt.ylabel("Frecuencia")
plt.show()