def contar_ocurrencias(cadena, subcadena):
    return cadena.count(subcadena)

# Ejemplo
cadena = input("Ingresa la cadena principal: ")
subcadena = input("Ingresa la subcadena a buscar: ")
ocurrencias = contar_ocurrencias(cadena, subcadena)
print(f"La subcadena '{subcadena}' aparece {ocurrencias} veces.")
