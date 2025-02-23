import random   #Importar librerias

def lanzar_dado():   #Definicion de funciones
    return random.randint(1, 6)

def lanzar_moneda():
    return random.choice(["Cara", "Cruz"])

print("Simulación de lanzamiento de dado y moneda") #Instrucciones
    
while True:
    print("1. Lanzar dado")
    print("2. Lanzar moneda")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":    #Switch
        print("Resultado del dado:", lanzar_dado())
    elif opcion == "2":
        print("Resultado de la moneda:", lanzar_moneda())
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intente de nuevo.")