import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", None)

clientes = pd.read_csv("clientes.csv")
ventas = pd.read_csv("ventas.csv")

resultado_union = pd.merge(clientes, ventas, on="id_cliente", how="inner")
print(resultado_union)

print("*" * 5)
resultado_left = pd.merge(clientes, ventas, on="id_cliente", how="left")
print(resultado_left)

print("*" * 5)
resultado_right = pd.merge(clientes, ventas, on="id_cliente", how="right")
print(resultado_right)

print("*" * 5)
resultado_outer = pd.merge(clientes, ventas, on="id_cliente", how="outer")
print(resultado_outer)
