import pandas as pd

# Lectura de archivos csv
data = pd.read_csv("ventas_enero.csv")
print(data)

# Lectura de archivos excel
data = pd.read_excel("ventas_enero_excel.xlsx")
print(data)

# Lectura de archivos excel sheet "otros"
data = pd.read_excel("ventas_enero_excel.xlsx", sheet_name="otros")
print(data)