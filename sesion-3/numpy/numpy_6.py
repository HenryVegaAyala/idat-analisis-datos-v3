import numpy as np

temperaturas = [22, 21, 23, 90, 22, 20, 105, 21]

# Convirtiendo a un array
temperaturas_array = np.array(temperaturas)

# Filtrando las temperaturas anómalas (mayores a 50 grados)
filtrado_anomalo = temperaturas_array > 50

# Resultado del filtrado
resultado = temperaturas_array[filtrado_anomalo]

print(f"Valores filtrados: {resultado}")
print(f"Cantidad de valores filtrados: {len(resultado)}")