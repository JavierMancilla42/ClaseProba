def contar_vocales_consonantes(palabra):
    palabra = palabra.lower()
    vocales = "aeiouáéíóú"
    consonantes = "bcdfghjklmnpqrstvwxyz"

    total_vocales = 0
    total_consonantes = 0

    for letra in palabra:
        if letra in vocales:
            total_vocales += 1
        elif letra in consonantes:
            total_consonantes += 1
    return total_vocales, total_consonantes

# Ejemplo
palabra = input("Ingresa una palabra: ")
vocales, consonantes = contar_vocales_consonantes(palabra)
print(f"Vocales: {vocales}")
print(f"Consonantes: {consonantes}")
