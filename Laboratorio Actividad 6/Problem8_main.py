# main.py
from Problem8_temperatura import convertir_celsius_a_fahrenheit as c_f
from Problem8_temperatura import convertir_fahrenheit_a_celsius as f_c

if __name__ == "__main__":
    while True:
        print("\n--- Conversión de Temperaturas ---")
        print("1. Celsius a Fahrenheit")
        print("2. Fahrenheit a Celsius")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            c = float(input("Ingresa la temperatura en °C: "))
            print(f"{c} °C = {c_f(c)} °F")
        elif opcion == "2":
            f = float(input("Ingresa la temperatura en °F: "))
            print(f"{f} °F = {f_c(f)} °C")
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
