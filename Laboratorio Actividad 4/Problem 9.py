def fusionar_listas_ordenadas(lista1, lista2):
    lista_combinada = lista1 + lista2
    return sorted(lista_combinada)

# Ejemplo
lista1 = [1, 3, 5, 7]
lista2 = [2, 4, 6, 8]
resultado = fusionar_listas_ordenadas(lista1, lista2)
print("Lista fusionada y ordenada:", resultado)

