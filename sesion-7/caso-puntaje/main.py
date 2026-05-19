import pandas as pd
import scipy.stats as st

df = pd.read_csv("puntaje.csv")

# Armamos 2 grupos
grupo_a = df[df["embalaje"] == "A"]["puntuacion"]  # filtro por embalaje tipo A --> Antiguo
grupo_b = df[df["embalaje"] == "B"]["puntuacion"] # filtro por embalaje tipo B --> Ecológico

# Realizamos el test de normalidad
resultado = st.ttest_ind(grupo_a, grupo_b)

# si el grupo A es menor al grupo B me va retorna negativo por lo tanto el grupo tiene mayor aceptación
# si el grupo A es mayor al grupo B me va retorna positivo por lo tanto el grupo no tiene aceptación

# Prueba T - Mostrar Resultado
print(f"Estadístico T: {resultado.statistic:.4f}")
print(f"Valor P: {resultado.pvalue:.4f}")

# Interpretación
if resultado.pvalue < 0.05:
    print("Hay diferencias significativas entre los grupos A y B.")
else:
    print("No hay diferencias significativas")