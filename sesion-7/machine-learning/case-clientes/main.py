import pandas as pd
from scipy.cluster.vq import kmeans
from sklearn.cluster import KMeans

df = pd.read_csv("clientes.csv")

x = df[["gasto_anual", "visitas_mes"]]

modelo = KMeans(n_clusters=2)
modelo.fit(x)

# Agrupador
df["cluster"] = modelo.labels_
print(df)

# Predicción
data_prediccion = pd.DataFrame([[500, 10]], columns=["gasto_anual", "visitas_mes"])
grupo_de_prueba = modelo.predict(data_prediccion)

print(f"Cliente pertenece al grupo: {grupo_de_prueba[0]}")

