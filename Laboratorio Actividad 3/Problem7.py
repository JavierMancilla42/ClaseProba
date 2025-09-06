def calcular_mediana(numeros):
    if not numeros:
        return None

    numeros.sort()
    n = len(numeros)
    medio = n // 2

    if n % 2 == 0:
        # Si la cantidad de elementos es par, se promedian los dos del centro
        mediana = (numeros[medio - 1] + numeros[medio]) / 2
    else:
        # Si es impar, la mediana es el valor del medio
        mediana = numeros[medio]

    return mediana

print(calcular_mediana([3, 1, 4]))