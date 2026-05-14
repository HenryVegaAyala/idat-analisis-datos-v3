import pandas as pd

sueldos = [1000, 1200, 1500, 1800]

df = pd.Series(sueldos)

print(df.mean())
