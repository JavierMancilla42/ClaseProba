def ordenar_por_longitud(palabras):
    return sorted(palabras, key=len)

# Ejemplo
entrada = input("Ingresa una lista de palabras separadas por espacios: ")
lista_palabras = entrada.split()
ordenadas = ordenar_por_longitud(lista_palabras)
print("Palabras ordenadas por longitud:", ordenadas)
