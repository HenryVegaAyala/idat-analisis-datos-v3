from pprint import pprint

import pandas as pd
import matplotlib.pyplot as plt

facturacion = pd.read_csv("facturacion.csv")
cliente = pd.read_csv("clientes.csv")

resultado = pd.merge(facturacion, cliente, on="id_cliente", how="left")

agrupador = resultado.groupby(["nombre", "pais"]).sum()["monto_total"]

# reiniciar indices
df_grafico = agrupador.reset_index()

df_grafico["etiqueta"] = df_grafico["nombre"] + " - " + df_grafico["pais"]

# Visualización grafica
plt.bar(df_grafico["etiqueta"], df_grafico["monto_total"], color=["green", "blue", "red"])
plt.xlabel("Clientes")
plt.ylabel("Monto Total")
plt.title("Facturación por cliente y País")
plt.show()

print("*" * 20)

barras = plt.bar(
    df_grafico["etiqueta"],
    df_grafico["monto_total"],
    color=["green", "blue", "red"],
)

for barra in barras:
    altura = barra.get_height()

    plt.text(
        barra.get_x() + barra.get_width() / 2,
        altura,
        f"{altura:.2f}",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold"
    )

# Linea de tendencia
plt.plot(
    df_grafico["etiqueta"],
    df_grafico["monto_total"],
    color="orange",
    marker="o",
    linestyle="--",
    linewidth=2,
    label="Tendencia"
)

plt.xlabel("Clientes")
plt.ylabel("Monto Total")
plt.title("Facturación por cliente y País")

plt.legend()
plt.xticks(rotation=20)
plt.tight_layout()

plt.show()