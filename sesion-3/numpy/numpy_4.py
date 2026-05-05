import numpy as np

edades = [5, 60, 20, 10, 15, 18, 24, 30]

array = np.array(edades)

es_mayor_de_edad = array >= 18
print(f"Resultado de la condicional: {es_mayor_de_edad}")

resultad = array[es_mayor_de_edad]
print(f"Edades mayores o iguales a 18: {resultad}")