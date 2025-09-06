def evaluar_polinomio(coeficientes, x):
    """
    coeficientes: lista de coeficientes del polinomio, comenzando por el coeficiente del término de mayor grado.
    x: el valor en el que se evaluará el polinomio.
    """
    resultado = 0
    grado = len(coeficientes) - 1
    for i, coef in enumerate(coeficientes):
        resultado += coef * (x ** (grado - i))
    return resultado

coeficientes = [3, 2, -1, 5]
x = 2

resultado = evaluar_polinomio(coeficientes, x)
print(resultado)