def registro_alumnos():
    alumnos = []

    while True:
        print("\nMenú:")
        print("1. Agregar alumno")
        print("2. Mostrar todos los alumnos")
        print("3. Salir")

        opcion = input("Elige una opción (1-3): ")

        if opcion == "1":
            nombre = input("Nombre del alumno: ")
            try:
                edad = int(input("Edad: "))
            except ValueError:
                print("Edad inválida. Debe ser un número entero.")
                continue
            
            calificaciones_input = input("Ingresa las calificaciones separadas por comas (ej: 7.5,8,9): ")
            try:
                calificaciones = tuple(float(nota.strip()) for nota in calificaciones_input.split(",") if nota.strip())
            except ValueError:
                print("Calificaciones inválidas. Asegúrate de ingresar números separados por comas.")
                continue
            
            alumno = (nombre, edad, calificaciones)
            alumnos.append(alumno)
            print(f"Alumno '{nombre}' agregado.")

        elif opcion == "2":
            if alumnos:
                for i, alumno in enumerate(alumnos, start=1):
                    nombre, edad, calificaciones = alumno
                    print(f"{i}. Nombre: {nombre}, Edad: {edad}, Calificaciones: {calificaciones}")
            else:
                print("No hay alumnos registrados.")

        elif opcion == "3":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

registro_alumnos()
