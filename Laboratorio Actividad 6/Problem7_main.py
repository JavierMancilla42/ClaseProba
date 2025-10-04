# main.py
from Problem6_circulo import calcular_area_circulo

radio = float(input("Ingresa el radio del círculo: "))
area = calcular_area_circulo(radio)
print(f"El área del círculo con radio {radio} es: {area:.2f}")