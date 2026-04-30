class Analista:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel

empleado_1 = Analista("Juan", "Senior")
print(f"Hola soy {empleado_1.nombre} y mi nivel es {empleado_1.nivel}")

