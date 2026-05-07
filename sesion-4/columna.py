import pandas as pd

data = pd.read_csv("ventas_enero.csv")

# Solo obtienes la serie de la columan seleccionada
print(data["producto"])

# Quiere tener multipples columas
print(data[["producto", "cantidad"]])