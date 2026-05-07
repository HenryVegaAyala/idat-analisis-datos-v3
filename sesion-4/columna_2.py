import pandas as pd

data = pd.read_excel("ventas_enero_excel.xlsx")

# Solo obtener una columna especifica.
serie = data["vendedor"]
print(serie)

# Quiero obtener varias columnas.
serie2 = data[["vendedor", "producto", "cantidad"]]
print(serie2)