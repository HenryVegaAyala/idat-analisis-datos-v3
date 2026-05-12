import matplotlib.pyplot as plt

edades = [20, 22, 21, 25, 30, 18, 19, 40, 45, 22, 23, 31]

plt.hist(edades, bins=5, color="red", edgecolor="black")

plt.title("Distribución de edades")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")

plt.grid(axis="y", alpha=0.3)

plt.show()