import numpy as np


class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

    def calcular_promedio(self):
        promedio = np.mean(self.notas)
        print(f"El estudiante {self.nombre} tiene un promedio de {promedio}")
        if promedio >= 11:
            print("El estudiante ha aprobado.")
        else:
            print("El estudiante ha reprobado.")

# Ejemplo de uso
estudiante_1 = Estudiante("Pepito", [10, 12, 9, 14])
estudiante_1.calcular_promedio()