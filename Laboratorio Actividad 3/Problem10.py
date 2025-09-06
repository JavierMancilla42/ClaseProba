def mcd(a, b):
    while b != 0:
        a, b = b, a % b  # El nuevo a es b, y el nuevo b es el resto de a dividido entre b
    return a

print(mcd(56, 98))