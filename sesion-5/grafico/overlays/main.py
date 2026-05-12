import matplotlib.pyplot as plt

mes = ["Enero", "Febrero", "Marzo", "Abril"]

luz = [40, 50, 45, 60]
agua = [25, 30, 28, 35]

plt.plot(mes, luz, label="Servicio de Luz", marker="o", linewidth=3, color="#ff9800")

plt.plot(mes, agua, label="Servicio de Agua", marker="s", linewidth=3, color="#2196f3")

plt.title("Gasto de la casa", fontsize=16, fontweight="bold")
plt.xlabel("Mes")
plt.ylabel("Gasto S/.")

plt.grid(True, linestyle="--", alpha=0.3)

for i, valor in enumerate(luz):
    plt.text(mes[i], valor +1, str(valor), ha="center")

for i, valor in enumerate(agua):
    plt.text(mes[i], valor +1, str(valor), ha="center")

plt.tight_layout()
plt.legend()
plt.show()
