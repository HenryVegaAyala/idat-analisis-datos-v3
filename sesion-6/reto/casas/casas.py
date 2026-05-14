import pandas as pd

df = pd.read_csv("casas.csv", skip_blank_lines=False)

cantidad_espacios = df["precios"].isnull().sum()

print(f"Cantidad de valores nullos en la columna precios: {cantidad_espacios}")

print(df.describe())