import pandas as pd

df = pd.read_csv("mascotas.csv")

moda = df["categoria"].mode().values[0]
promedio = df["precio"].mean()

print(f"La moda es: {moda}")
print(f"La promedio es: {promedio}")