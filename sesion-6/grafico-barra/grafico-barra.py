import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('salario.csv')

# Filtrado por sueldos mayor a 5000
df_filtrado = df[df['sueldo'] >= 5000]

nombre = df_filtrado["nombre"]
sueldo = df_filtrado["sueldo"]

plt.figure(figsize=(20, 6))

plt.bar(nombre, sueldo)

plt.xticks(rotation=90)
plt.tight_layout()

plt.show()