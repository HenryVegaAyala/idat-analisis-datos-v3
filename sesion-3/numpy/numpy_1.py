import numpy as np

# Listado de números enteros
lista = [10, 20, 30, 40]

# Conversión a un vector con numpy
array = np.array(lista)

print(f"Listado original: {lista}")
print(f"Convertido en array: {array}")

zeros = np.zeros(5)
print(f"Array de ceros: {zeros}")

unos = np.ones(3)
print(f"Array de unos: {unos}")

rango = np.arange(0, 10, 2)
print(f"Array con rango de 0 a 10 con paso de 2: {rango}")
