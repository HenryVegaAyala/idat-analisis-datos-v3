import pandas as pd

data = pd.read_csv("ventas_enero.csv")

# Forma del paso a paso
filtrado_de_cantidad = data["cantidad"] >= 5
resultado = data[filtrado_de_cantidad]
print(resultado)

# Forma directa
resultado = data[data["cantidad"] >= 5]
print(resultado)