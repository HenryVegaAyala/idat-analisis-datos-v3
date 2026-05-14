import pandas as pd

df = pd.read_csv("notas.csv")

print(df["notas"].mean())
print(df["notas"].median())