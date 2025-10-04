def promedio(lista):
    if not lista:
        raise ValueError("La lista no puede estar vacía")
    return sum(lista) / len(lista)

# Implementacion
numeros = [10, 20, 30, 40, 50]
print("Lista:", numeros)
print("Promedio:", promedio(numeros))