import pandas as pd

facturacion = pd.read_csv("facturacion.csv")
cliente = pd.read_csv("clientes.csv")

resultado = pd.merge(facturacion, cliente, on="id_cliente", how="left")
print(resultado)

agrupador = resultado.groupby(["nombre", "pais"]).sum()["monto_total"]
print(agrupador)

# Exportar resultados.
agrupador.to_csv("agrupador.csv")