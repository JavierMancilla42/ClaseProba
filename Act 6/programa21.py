import math   #Importara librerias

def area_cuadrado(lado):   #Definicion de funciones
    return lado ** 2

def area_rectangulo(base, altura):
    return base * altura

def area_circulo(radio):
    return math.pi * radio ** 2

def volumen_cubo(lado):
    return lado ** 3

def volumen_esfera(radio):
    return (4/3) * math.pi * radio ** 3

def volumen_cilindro(radio, altura):
    return math.pi * radio ** 2 * altura

#Seleccion de opciones
print("Calculadora de Áreas y Volúmenes")
print("1. Área de un cuadrado")
print("2. Área de un rectángulo")
print("3. Área de un círculo")
print("4. Volumen de un cubo")
print("5. Volumen de una esfera")
print("6. Volumen de un cilindro")
opcion = int(input("Seleccione una opción: "))
    
if opcion == 1:   #Switch
   lado = float(input("Ingrese el lado del cuadrado: "))
   print("Área del cuadrado:", area_cuadrado(lado))
elif opcion == 2:
   base = float(input("Ingrese la base del rectángulo: "))
   altura = float(input("Ingrese la altura del rectángulo: "))
   print("Área del rectángulo:", area_rectangulo(base, altura))
elif opcion == 3:
   radio = float(input("Ingrese el radio del círculo: "))
   print("Área del círculo:", area_circulo(radio))
elif opcion == 4:
   lado = float(input("Ingrese el lado del cubo: "))
   print("Volumen del cubo:", volumen_cubo(lado))
elif opcion == 5:
   radio = float(input("Ingrese el radio de la esfera: "))
   print("Volumen de la esfera:", volumen_esfera(radio))
elif opcion == 6:
   radio = float(input("Ingrese el radio del cilindro: "))
   altura = float(input("Ingrese la altura del cilindro: "))
   print("Volumen del cilindro:", volumen_cilindro(radio, altura))
else:
   print("Opción no válida")