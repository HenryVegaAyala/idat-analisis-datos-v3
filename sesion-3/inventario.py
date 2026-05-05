class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad):
        self.stock = self.stock + cantidad
        print(f"Cantidad de productos: {self.nombre} - {self.stock} unidades")

laptops = Producto("Laptop Asus", 2000, 20)
laptops.actualizar_stock(10)
laptops.actualizar_stock(-20)