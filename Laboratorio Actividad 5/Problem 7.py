def diccionario_traduccion():
    traducciones = {}

    while True:
        print("\nMenú:")
        print("1. Agregar una traducción")
        print("2. Buscar una traducción")
        print("3. Ver todas las palabras registradas")
        print("4. Salir")

        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            palabra_origen = input("Ingresa la palabra en el idioma original: ").lower()
            palabra_traduccion = input("Ingresa su traducción: ").lower()
            traducciones[palabra_origen] = palabra_traduccion
            print(f"Traducción agregada: {palabra_origen} -> {palabra_traduccion}")

        elif opcion == "2":
            palabra = input("Palabra a traducir: ").lower()
            if palabra in traducciones:
                print(f"Traducción de '{palabra}': {traducciones[palabra]}")
            else:
                print(f"La palabra '{palabra}' no está registrada.")

        elif opcion == "3":
            if traducciones:
                print("Palabras registradas:")
                for palabra in traducciones.keys():
                    print(palabra)
            else:
                print("No hay palabras registradas aún.")

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

# Implementacion
diccionario_traduccion()
