class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def hacer_sonido(self):
        if self.especie == "Felino":
            return "Miau"
        elif self.especie == "Canino":
            return "Guau"
        else:
            return "Sonido desconocido"

# Crear una nueva instancia
gato = Animal("Pelusa", "Felino")
print(f"Soy {gato.nombre} y soy un {gato.especie} y hago {gato.hacer_sonido()}")

perro = Animal("Mailo", "Canino")
print(f"Soy {perro.nombre} y soy un {perro.especie} y hago {perro.hacer_sonido()}")

nombre = input("Ingrese el nombre del animal: ")
especie = input("Ingrese la especie del animal (Felino/Canino): ")
animal = Animal(nombre, especie)
print(f"Soy {animal.nombre} y soy un {animal.especie} y hago {animal.hacer_sonido()}")