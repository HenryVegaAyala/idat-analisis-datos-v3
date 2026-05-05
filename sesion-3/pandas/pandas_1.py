import pandas as pd

# Paso 2 definir un diccionario
datos = {
    "Nombre": ["Juan", "María", "Pedro", "Ana"],
    "Edad": [25, 30, 22, 28]
}

# Paso 3 convertir a un dataframe
df = pd.DataFrame(datos)

print(df)