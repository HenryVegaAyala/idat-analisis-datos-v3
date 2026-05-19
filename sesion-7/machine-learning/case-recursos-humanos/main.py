import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("regresion_multiple.csv")

x = df[["experiencia", "estudios"]] # Variable X que es la causa
y = df["salario"] # Variable Y que es el efecto

modelo = LinearRegression()
modelo.fit(x, y)

prediccion_salario = pd.DataFrame([[4, 5]], columns=["experiencia", "estudios"])

resultado_salario = modelo.predict(prediccion_salario)
print(f"salario sugerido: {resultado_salario[0]:.2f}")