def convertir_a_soles(dolares, tipo_de_cambio=3.80):
    conversion_soles = dolares * tipo_de_cambio
    return conversion_soles

# Caso N° 1 - Dolares y tipo de cambio por defecto
resultado = convertir_a_soles(100)
print(f"El resultado es: {resultado}")

# Caso N° 2 - Dolares y tipo de cambio a 4.1
resultado = convertir_a_soles(100, 4.1)
print(f"El resultado es: {resultado}")