import numpy as np

edades = [10, 20, 30, 5, 9, 30, 10, 30, 90, 10]

# Convetir a un vector
array = np.array(edades)

filtro_de_menor_de_edad = array <= 18
print(f"Resultado de la condicional: {filtro_de_menor_de_edad}")

resultado = array[filtro_de_menor_de_edad]
print(f"Resultado de la condicional: {resultado}")