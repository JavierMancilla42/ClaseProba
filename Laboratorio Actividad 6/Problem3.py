def contar_vocales(cadena):
    cadena = cadena.lower()
    vocales = "aeiou"
    resultado = []

    for v in vocales:
        cantidad = cadena.count(v)
        resultado.append((v, cantidad))

    return resultado

# Implementacion
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print("Cadena:", texto)
print("Conteo de vocales:", contar_vocales(texto))