def agenda_contactos():
    agenda = {}

    while True:
        print("Agenda de Contactos")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Ver todos los contactos")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ")

        #Switch
        if opcion == "1":
            nombre = input("Nombre del contacto: ")
            telefono = input("Número de teléfono: ")
            agenda[nombre] = telefono
            print(f"Contacto '{nombre}' agregado.")

        elif opcion == "2":
            nombre = input("Nombre del contacto a buscar: ")
            if nombre in agenda:
                print(f"{nombre}: {agenda[nombre]}")
            else:
                print("Contacto no encontrado.")

        elif opcion == "3":
            nombre = input("Nombre del contacto a eliminar: ")
            if nombre in agenda:
                del agenda[nombre]
                print(f"Contacto '{nombre}' eliminado.")
            else:
                print("Contacto no encontrado.")

        elif opcion == "4":
            if agenda:
                print("Lista de contactos:")
                for nombre, telefono in agenda.items():
                    print(f"{nombre}: {telefono}")
            else:
                print("La agenda está vacía.")

        elif opcion == "5":
            print("Saliendo de la agenda.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

# Implementacion
agenda_contactos()
