def factorial(n):
    if n < 0:
        raise ValueError("El número debe ser un entero no negativo")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Implementacion
numero = 5
print(f"{numero}! =", factorial(numero))