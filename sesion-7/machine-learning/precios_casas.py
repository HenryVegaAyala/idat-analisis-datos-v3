from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = fetch_california_housing()
x, y = data.data, data.target

# Dividir el dataset en entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Modelo
model = LinearRegression()
model.fit(x_train, y_train)

# Predicción en futuro
y_pred = model.predict(x_test)

print("MSE: ", mean_squared_error(y_test, y_pred))

nueva_casa = [[3, 25, 5, 1, 1500, 3, 34, -118]]
print(f"Precio estimado: {model.predict(nueva_casa)}")