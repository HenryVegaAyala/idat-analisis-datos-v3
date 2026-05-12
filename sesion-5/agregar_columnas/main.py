import pandas as pd
import random

df = pd.read_csv('ventas_enero.csv')

df["total"] = df["cantidad"] * df["precio_unitario"]
df["fecha_creacion"] = pd.to_datetime("2026-04-05")
df["fecha_random"] = [
    (
        pd.Timestamp.now() +
        pd.to_timedelta(random.randint(0, 365), unit="D")
    ).strftime("%Y-%m-%d")
    for _ in range(len(df))
]

print(df)
