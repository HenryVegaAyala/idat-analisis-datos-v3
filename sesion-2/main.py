# 1. Crear una lista de productos
vitrina = ["Pan", "Alfajor", "Aceite", "Mantequilla"]

# 2. Listado de números
ventas_horas_ = [10, 20, 15, 30]

# 3. Acceder al primer elemento (indice 0)
primer_producto = vitrina[0]
print(f"Primer producto: {primer_producto}")

# 4. Acceder al ultimo elemento (indice -1)
ultimo_producto = vitrina[-1]
print(f"Ultimo producto: {ultimo_producto}")

# 5. Contar cuantos elementos hay en una lista
total_productos = len(vitrina)
print(f"Total productos: {total_productos}")

# 6. Agregar un nuevo producto a la lista
vitrina.append("Donut")
print(f"Lista de productos agregados: {vitrina}")

# 7. Cambiar o actualizar un producto de la lista
vitrina[2] = "Aceite de oliva"
print(f"Lista de productos actualizados: {vitrina}")

# 8. Eliminar un producto de la lista
vitrina.remove("Pan")
print(f"Lista de productos eliminados: {vitrina}")

# 9. Eliminar con metodo "del" de la lista
del vitrina[0]
print(f"Lista de productos eliminados con del: {vitrina}")

# 10. Uso de "pop" para lista
print(f"Vitrina antes de usar pop: {vitrina}")
producto_eliminado = vitrina.pop(1)
print(f"Vitrina despues de usar pop: {vitrina}")
print(f"Producto eliminado con pop: {producto_eliminado}")

# 11. Verificar si existe un producto en la lista
existe_donut = "Donut" in vitrina
print(f"¿Existe donut?: {existe_donut}")