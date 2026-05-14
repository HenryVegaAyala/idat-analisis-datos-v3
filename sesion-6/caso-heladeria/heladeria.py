import pandas as pd
import numpy as np
import scipy.stats as st

# 1. Leer y cargar datos en memoria
df = pd.read_csv("gastos.csv")
dato_de_gastos = df["gasto"]

# 2. Calcular el intervalo de confianza 95%

intervalo = st.t.interval(
    confidence=0.95,  # porcentaje de intervalo de confianza
    df=len(dato_de_gastos) - 1,  # Ajuste de cantidad de datos
    loc=np.mean(dato_de_gastos),  # media de los datos -> promedio
    scale=st.sem(dato_de_gastos),  # error estándar de la media
)

print(f"El cliente promedio gastara entre s/.{intervalo[0]} y s/.{intervalo[1]}")

# Punto medio
promedio = (intervalo[0] + intervalo[1]) / 2
print(promedio) # 15.43

# marge de error -> 1.89
print(15.43 - intervalo[0])
print(intervalo[1] - 15.43)