import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", None)

enero = pd.read_csv("ventas_enero.csv")
febrero = pd.read_csv("ventas_febrero.csv")

anual = pd.concat([enero, febrero])

print(anual)