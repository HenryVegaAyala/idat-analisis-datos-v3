import matplotlib.pyplot as plt

semana = [1, 2, 3, 4]
km_recorridos = [2, 5, 4, 8]

plt.plot(semana, km_recorridos)
plt.title("Recorridos en km")

plt.xlabel("semana")
plt.ylabel("km")

plt.show()
