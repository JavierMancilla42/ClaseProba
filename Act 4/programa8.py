#Importar libreria
import math as mt

print("Programa para calcular el área y la circunferencia de un circulo")

#input
r = float(input("Elija el radio del circulo: "))

a=mt.pi*r**2
c=2*mt.pi*r

print("El area del circulo es:", a)
print("La circunferencia del circulo es:", c)