import pandas as pd

df = pd.read_csv('ventas_enero.csv')

df.drop("id_venta", axis=1, inplace=True)

print(df)
