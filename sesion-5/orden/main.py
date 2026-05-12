import pandas as pd

df = pd.read_csv('ventas_enero.csv')

resultado = df[df["precio_unitario"] > 1000]

print(resultado)