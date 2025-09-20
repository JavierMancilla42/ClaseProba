def eliminar_impares(lista):
    return [numero for numero in lista if numero % 2 == 0]

# Ejemplo
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
solo_pares = eliminar_impares(numeros)
print("Lista con solo números pares:", solo_pares)