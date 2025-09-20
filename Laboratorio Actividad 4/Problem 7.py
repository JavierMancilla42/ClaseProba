def obtener_iniciales(nombre_completo):
    partes = nombre_completo.strip().split()
    iniciales = ''.join([parte[0].upper() for parte in partes])
    return iniciales

# Ejemplo
nombre = input("Ingresa el nombre completo: ")
resultado = obtener_iniciales(nombre)
print("Iniciales:", resultado)
