def diccionario_notas():
    notas_estudiantes = {}

    while True:
        print("\nMenú:")
        print("1. Agregar notas de un estudiante")
        print("2. Ver notas de un estudiante")
        print("3. Ver todos los estudiantes y sus notas")
        print("4. Salir")

        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            nombre = input("Nombre del estudiante: ").capitalize()
            notas = input("Ingresa las notas separadas por comas (ej: 8.5,9.0,7): ")

            try:
                lista_notas = [float(nota.strip()) for nota in notas.split(",")]
                if nombre in notas_estudiantes:
                    notas_estudiantes[nombre].extend(lista_notas)
                else:
                    notas_estudiantes[nombre] = lista_notas
                print(f"Notas agregadas para {nombre}")
            except ValueError:
                print("Error: Asegúrate de ingresar solo números separados por comas.")

        elif opcion == "2":
            nombre = input("Nombre del estudiante: ").capitalize()
            if nombre in notas_estudiantes:
                print(f"Notas de {nombre}: {notas_estudiantes[nombre]}")
            else:
                print("Estudiante no encontrado.")

        elif opcion == "3":
            if notas_estudiantes:
                for estudiante, notas in notas_estudiantes.items():
                    print(f"{estudiante}: {notas}")
            else:
                print("No hay estudiantes registrados.")

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

# Implementacion
diccionario_notas()
