def calcular_precio_final(precio_del_producto):
    igv = 0.19
    impuesto = precio_del_producto * igv
    total = precio_del_producto + impuesto

    return total

producto_a = calcular_precio_final(100)
print(f"Resultado final: {producto_a}")