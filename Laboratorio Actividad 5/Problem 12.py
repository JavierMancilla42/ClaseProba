def registro_estudiantes():
    estudiantes = {}

    while True:
        print("\nMenú:")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiante")
        print("3. Mostrar todos los estudiantes")
        print("4. Salir")

        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            nombre = input("Nombre del estudiante: ").capitalize()

            # Ingresar asignaturas y calificaciones
            asignaturas = {}
            print("Ingresa las asignaturas y calificaciones. Para terminar escribe 'fin' en el nombre de la asignatura.")
            while True:
                asignatura = input("Asignatura: ").strip()
                if asignatura.lower() == "fin":
                    break
                try:
                    nota = float(input(f"Calificación para {asignatura}: "))
                    asignaturas[asignatura] = nota
                except ValueError:
                    print("Calificación inválida. Intenta de nuevo.")

            # Ingresar lista de amigos
            amigos = []
            print("Ingresa los nombres de los amigos. Para terminar escribe 'fin'.")
            while True:
                amigo = input("Nombre del amigo: ").capitalize()
                if amigo.lower() == "fin":
                    break
                amigos.append(amigo)

            # Guardar estudiante
            estudiantes[nombre] = {
                "asignaturas": asignaturas,
                "amigos": amigos
            }
            print(f"Estudiante '{nombre}' agregado.")

        elif opcion == "2":
            nombre = input("Nombre del estudiante a mostrar: ").capitalize()
            if nombre in estudiantes:
                info = estudiantes[nombre]
                print(f"\nEstudiante: {nombre}")
                print("Asignaturas y calificaciones:")
                for asignatura, nota in info["asignaturas"].items():
                    print(f"  {asignatura}: {nota}")
                print("Amigos:")
                if info["amigos"]:
                    for amigo in info["amigos"]:
                        print(f"  {amigo}")
                else:
                    print("  No tiene amigos registrados.")
            else:
                print("Estudiante no encontrado.")

        elif opcion == "3":
            if estudiantes:
                for nombre, info in estudiantes.items():
                    print(f"\nEstudiante: {nombre}")
                    print("Asignaturas y calificaciones:")
                    for asignatura, nota in info["asignaturas"].items():
                        print(f"  {asignatura}: {nota}")
                    print("Amigos:")
                    if info["amigos"]:
                        for amigo in info["amigos"]:
                            print(f"  {amigo}")
                    else:
                        print("  No tiene amigos registrados.")
            else:
                print("No hay estudiantes registrados.")

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

# Implementacion
registro_estudiantes()
