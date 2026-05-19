from unittest import result

import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("regresion_logistica.csv")

x = df[["antiguedad", "cuota_mensual"]]
y = df["fuga"]

modelo = LogisticRegression()
modelo.fit(x, y)

prediccion_fuga = pd.DataFrame([[1, 35]], columns=["antiguedad", "cuota_mensual"])
resultado = modelo.predict(prediccion_fuga)

if resultado[0] == 1:
    print("el cliente va hacer churn")
else:
    print("el cliente se va a quedar con el servicio un mes más")