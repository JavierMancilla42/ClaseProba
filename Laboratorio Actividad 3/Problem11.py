def determinante_3x3(matriz):
    if len(matriz) != 3 or any(len(fila) != 3 for fila in matriz):
        raise ValueError("La matriz debe ser de 3x3")

    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]

    determinante = (a * e * i + b * f * g + c * d * h) - (c * e * g + b * d * i + a * f * h)
    return determinante

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(determinante_3x3(matriz))