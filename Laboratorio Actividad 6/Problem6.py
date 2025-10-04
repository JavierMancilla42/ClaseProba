def fibonacci(n):
    if n < 0:
        raise ValueError("n debe ser un entero no negativo")

    # Definición recursiva
    def fib(k):
        if k == 0:
            return 0
        elif k == 1:
            return 1
        else:
            return fib(k-1) + fib(k-2)

    # Construir lista con la serie hasta n
    serie = [fib(i) for i in range(n+1)]
    return serie[-1], serie

# Implementacion
n = 7
termino, serie = fibonacci(n)
print(f"El término {n} de Fibonacci es:", termino)
print("Secuencia hasta", n, ":", serie)