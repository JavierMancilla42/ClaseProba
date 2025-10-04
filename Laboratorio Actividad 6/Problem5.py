def suma_naturales(n):
    if n < 0:
        raise ValueError("El número debe ser un entero no negativo")
    if n == 0:
        return 0
    return n + suma_naturales(n - 1)

# Implementacion
n = 5
print(f"Suma de los primeros {n} números naturales:", suma_naturales(n))