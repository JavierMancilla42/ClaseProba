def eliminar_espacios_extra(cadena):
    palabras = cadena.split()
    resultado = ' '.join(palabras)
    return resultado

# Ejemplo
entrada = input("Ingresa una frase con espacios extra: ")
salida = eliminar_espacios_extra(entrada)
print("Frase corregida:", salida)