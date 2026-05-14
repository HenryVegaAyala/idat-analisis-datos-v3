import matplotlib.pyplot as plt

mes = ["Enero", "Febrero", "Marzo", "Abril"]
luz = [40, 50, 45, 60]
agua = [25, 30, 28, 35]

# Crear subplots
fig, ax = plt.subplots(3,1, figsize = (10,6))

# fig -> Representa la figura completa
# ax -> Representa cada uno de los gráficos

ax[0].plot(mes, luz, marker = "o", color = "blue", label = "servicio de luz eléctrica")
ax[0].set_title("Gastos de servicio de luz")
ax[0].set_ylabel("Costo")

ax[1].plot(mes, agua, marker = "o", color = "orange", label = "servicio de luz agua potable")
ax[1].set_title("Gastos de servicio de agua potable")
ax[1].set_ylabel("Costo")

ax[2].bar(mes, luz)
ax[2].set_title("Gastos de Luz (Barras)")

# para ajustar los espacios
plt.tight_layout()

plt.show()