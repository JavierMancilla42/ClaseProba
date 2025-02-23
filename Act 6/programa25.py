import random    #Importar librerias
import matplotlib.pyplot as plt

def lanzar_dado():    #Definicion de funciones
    return random.randint(1, 6)

def lanzar_moneda():
    return random.choice(["Cara", "Cruz"])

def mostrar_histograma(resultados, titulo, etiquetas):
    plt.hist(resultados, bins=range(len(etiquetas) + 1), align='left', rwidth=0.8)
    plt.xticks(range(len(etiquetas)), etiquetas)
    plt.xlabel("Resultados")
    plt.ylabel("Frecuencia")
    plt.title(titulo)
    plt.show()

print("Simulación de lanzamiento de dado y moneda")    #Instrucciones
lanzamientos_dado = []
lanzamientos_moneda = []

while True:
    print("\n1. Lanzar dado")
    print("2. Lanzar moneda")
    print("3. Mostrar histograma del dado")
    print("4. Mostrar histograma de la moneda")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":    #Switch
        resultado = lanzar_dado()
        lanzamientos_dado.append(resultado)
        print("Resultado del dado:", resultado)
    elif opcion == "2":
        resultado = lanzar_moneda()
        lanzamientos_moneda.append(resultado)
        print("Resultado de la moneda:", resultado)
    elif opcion == "3":
        if lanzamientos_dado:
            mostrar_histograma(lanzamientos_dado, "Histograma de lanzamientos del dado", ["1", "2", "3", "4", "5", "6"])
        else:
            print("No hay datos para mostrar el histograma del dado.")
    elif opcion == "4":
        if lanzamientos_moneda:
            mostrar_histograma(lanzamientos_moneda, "Histograma de lanzamientos de la moneda", ["Cara", "Cruz"])
        else:
            print("No hay datos para mostrar el histograma de la moneda.")
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intente de nuevo.")