import pandas as pd
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("dato_credito.csv")

x = df[["ingreso", "morosidad"]]

y = df["aprobado"]

modelo = DecisionTreeClassifier()
modelo.fit(x, y)

prediccion_credito = pd.DataFrame([[1200, 0]], columns=["ingreso", "morosidad"])
resultado_credito = modelo.predict(prediccion_credito)

if resultado_credito == 1:
    print("El crédito ha sido aprobado.")
else:
    print("El credito ha sido rechazado.")