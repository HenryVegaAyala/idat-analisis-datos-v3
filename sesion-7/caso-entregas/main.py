import pandas as pd
import scipy.stats as st
import numpy as np

df = pd.read_csv("tiempos.csv")

# Paso 1: Filtrar los datos
vehiculo_tradicional = df[df["vehiculo"] == "Tradicional"]["minutos"]
vehiculo_electrico = df[df["vehiculo"] == "Electrica"]["minutos"]

# Paso 2: Intervalo de confianza

# Promedio de tiempo del vehículo tradicional
promedio_tradicional = np.mean(vehiculo_tradicional)

# Promedio de tiempo del vehículo eléctrico
promedio_electrico = np.mean(vehiculo_electrico)

print(f"Promedios:")
print(f"Promedio tradicional: {promedio_tradicional:.2f} minutos")
print(f"Promedio Eléctrico: {promedio_electrico:.2f} minutos")

# Resultado esperado:
# Tradicional = 28.2 minutos
# Eléctrico = 20 minutos

print("-" * 30)

ic_tradicional = st.t.interval(
    confidence=0.95,  # Nivel de confianza al 95%
    df=len(vehiculo_tradicional) - 1,  # Grados de libertad de cantidad de datos - 1
    loc=promedio_tradicional,  # Promedio de los datos
    scale=st.sem(vehiculo_tradicional)  # Error estándar
)

print(f"Intervalo de confianza para el vehículo tradicional:")
print(f"Entre {ic_tradicional[0]:.2f} y {ic_tradicional[1]:.2f} minutos")
print(f"Promedio del vehículo tradicional: {(ic_tradicional[0] + ic_tradicional[1]) / 2:.2f} minutos")

print("-" * 30)

ic_electrico = st.t.interval(
    confidence=0.95,  # Nivel de confianza al 95%
    df=len(vehiculo_electrico) - 1,  # Grados de libertad de cantidad de datos - 1
    loc=promedio_electrico,  # Promedio de los datos
    scale=st.sem(vehiculo_electrico)  # Error estándar
)

print(f"Intervalo de confianza para el vehículo eléctrico:")
print(f"Entre {ic_electrico[0]:.2f} y {ic_electrico[1]:.2f} minutos")
print(f"Promedio del vehículo eléctrico: {(ic_electrico[0] + ic_electrico[1]) / 2:.2f} minutos")

print("-" * 30)

# Paso 3: Prueba test A/B

test = st.ttest_ind(vehiculo_tradicional, vehiculo_electrico)
print(f"Prueba: ")
print(f"Valor p: {test.pvalue:.4f}")

if test.pvalue < 0.05:
    print("Existe una diferencia significativa entre ambos vehículos.")
else:
    print("No existe una diferencia significativa entre ambos vehículos.")