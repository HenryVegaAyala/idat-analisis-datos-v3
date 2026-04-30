# def = definición
# saludo_inicial = Nombre de la funcion a reutilizar
# nombre = parametro
# : = El delimitado o cierre de la funcion
# return = palabra reservada para devolver un valor

def saludo_inicial(nombre):
    saludo = f"Hola Mundo, soy {nombre} un gusto saludate."
    return saludo

saludo = saludo_inicial("Luis")
print(saludo)

saludo_2 = saludo_inicial("Israel")
print(saludo_2)