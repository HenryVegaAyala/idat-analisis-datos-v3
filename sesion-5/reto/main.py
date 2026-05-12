import pandas as pd

df = pd.read_csv('ventas_enero.csv')

ordenamiento = df.sort_values("vendedor")
print(ordenamiento)

ordenamiento_multiple = df.sort_values(["vendedor", "precio_unitario"])
print(ordenamiento_multiple)