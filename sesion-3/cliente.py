class Cliente:
    def __init__(self, nombre_cliente, saldo):
        self.nombre_cliente = nombre_cliente
        self.saldo = saldo

    def comprar_producto(self, monto, producto):
        if self.saldo >= monto:
            self.saldo = self.saldo - monto
            print(f"{self.nombre_cliente} ha comprado exitosamente un {producto}, le queda un saldo de {self.saldo}")
        else:
            print(f"{self.nombre_cliente} no tiene suficiente saldo para comprar un {producto}")


cliente_1 = Cliente("Tania", 1000)
cliente_1.comprar_producto(900, "Celular")
cliente_1.comprar_producto(50, "Galleta")
cliente_1.comprar_producto(40, "Funda de celular")

cliente_2 = Cliente("Pablo", 2000)
cliente_2.comprar_producto(1500, "Laptop")
