import pandas as pd

df = pd.read_csv('ventas_enero.csv')

df.rename(columns={"vendedor": "Cliente"}, inplace=True)

print(df)
