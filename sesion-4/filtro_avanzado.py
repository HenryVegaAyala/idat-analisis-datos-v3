import pandas as pd

data = pd.read_csv("ventas_enero.csv")

# Armando los filtados
filtrado_de_cantidad = data["cantidad"] >= 1
filtrado_de_precio = data["precio_unitario"] > 1000

resultados = data[(filtrado_de_cantidad) & (filtrado_de_precio)]
print(resultados)