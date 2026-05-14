import pandas as pd

edades = [10, 12, 10, 11, None, 85, 11]

df = pd.Series(edades)

# calcular la media de las edades, ignorando los valores nulos
mediana = df.median()
print(f"Mediana sugerida {mediana}")

# Reemplazar valores Nan
edades_corregidas = df.fillna(mediana)

resultado = edades_corregidas[edades_corregidas <= 18]

print(resultado)