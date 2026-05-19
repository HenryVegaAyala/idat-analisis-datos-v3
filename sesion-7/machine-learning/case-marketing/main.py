import pandas as pd
from sklearn.linear_model import LinearRegression

# Leer archivo csv
data = pd.read_csv("marketing.csv")

# seleccionamos la columna marketing en un dataframe en lugar de una serie "LinearRegression espera un array 2D"
x = data[["marketing"]]
print(x)

# seleccionamos la columna ventas como una serie
y = data["ventas"]
print(y)

# Comenzamos a entrenar el modelo de regresion lineal
modelo = LinearRegression()
modelo.fit(x, y) # Se entrena el modelo de datos con los resultados de Marketing (x) y Ventas (y)

# Creamos el registro de predicción para el nuevo gasto de marketing
nueva_fila_marketing = pd.DataFrame([[6000]], columns=["marketing"])
prediccion = modelo.predict(nueva_fila_marketing)
print(prediccion)
print(f"La predicción de ventas para una inversion de $6000 en marketing: {prediccion[0]:.2f}")

# Creamos el registro de predicción para el nuevo gasto de marketing
nueva_fila_marketing = pd.DataFrame([[10000]], columns=["marketing"])
prediccion = modelo.predict(nueva_fila_marketing)
print(f"La predicción de ventas para una inversion de $10000 en marketing: {prediccion[0]:.2f}")