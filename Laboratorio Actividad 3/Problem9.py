def segundo_mayor(numeros):
    if len(numeros) < 2:
        return None

    numeros_unicos = set(numeros)
    if len(numeros_unicos) < 2:
        return None 

    numeros_unicos.remove(max(numeros_unicos))
    return max(numeros_unicos)

print(segundo_mayor([1, 2, 3, 4, 5]))