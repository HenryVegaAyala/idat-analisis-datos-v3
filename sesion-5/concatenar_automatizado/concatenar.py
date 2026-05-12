import glob
import pandas as pd
import os

# Configuraciones visualizes
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", None)

# Buscar todos los archivos CSV automáticamente
archivos_csv = glob.glob("*.csv")

dataframes = []

# Leer y unificar todos los archivos csv:
for archivo in archivos_csv:
    df = pd.read_csv(archivo)
    df["archivo_origin"] = os.path.basename(archivo)
    dataframes.append(df)

anual = pd.concat(dataframes, ignore_index=True)

print(anual)