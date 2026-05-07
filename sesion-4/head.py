import pandas as pd
from pandas import read_csv

data = read_csv("ventas_enero.csv")

print(data.head(1))