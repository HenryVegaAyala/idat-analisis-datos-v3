from pprint import pprint

import pandas as pd
import matplotlib.pyplot as plt

facturacion = pd.read_csv("facturacion.csv")
cliente = pd.read_csv("clientes.csv")

resultado = pd.merge(facturacion, cliente, on="id_cliente", how="left")

agrupador = resultado.groupby(["nombre", "pais"]).sum()["monto_total"]
print(agrupador)

# reiniciar indices
df_grafico = agrupador.reset_index()

df_grafico["etiqueta"] = df_grafico["nombre"] + " - " + df_grafico["pais"]

print(df_grafico)

# Visualización grafica
plt.bar(df_grafico["etiqueta"], df_grafico["monto_total"], color=["green", "blue", "red"])
plt.xlabel("Clientes")
plt.ylabel("Monto Total")
plt.title("Facturación por cliente y País")
plt.show()
