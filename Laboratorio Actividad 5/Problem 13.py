def agenda_contactos():
    agenda = []

    #Funciones
    def agregar_contacto():
        nombre = input("Nombre del contacto: ").strip()
        telefono = input("Número de teléfono: ").strip()

        correos = []
        print("Ingresa los correos electrónicos. Escribe 'fin' para terminar.")
        while True:
            correo = input("Correo electrónico: ").strip()
            if correo.lower() == 'fin':
                break
            correos.append(correo)

        contacto = {
            "nombre": nombre,
            "telefono": telefono,
            "correos": correos
        }
        agenda.append(contacto)
        print(f"Contacto '{nombre}' agregado.")

    def buscar_contacto():
        nombre_buscar = input("Nombre del contacto a buscar: ").strip().lower()
        encontrados = [c for c in agenda if c["nombre"].lower() == nombre_buscar]
        if encontrados:
            for c in encontrados:
                print(f"\nNombre: {c['nombre']}")
                print(f"Teléfono: {c['telefono']}")
                if c['correos']:
                    print("Correos electrónicos:")
                    for correo in c['correos']:
                        print(f" - {correo}")
                else:
                    print("No tiene correos electrónicos.")
        else:
            print("No se encontró el contacto.")

    def eliminar_contacto():
        nombre_eliminar = input("Nombre del contacto a eliminar: ").strip().lower()
        for i, c in enumerate(agenda):
            if c["nombre"].lower() == nombre_eliminar:
                del agenda[i]
                print(f"Contacto '{c['nombre']}' eliminado.")
                return
        print("No se encontró el contacto para eliminar.")

    #Switch
    while True:
        print("\nMenú:")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar todos los contactos")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ")

        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            eliminar_contacto()
        elif opcion == "4":
            if agenda:
                print("\nContactos en la agenda:")
                for c in agenda:
                    print(f"\nNombre: {c['nombre']}")
                    print(f"Teléfono: {c['telefono']}")
                    if c['correos']:
                        print("Correos electrónicos:")
                        for correo in c['correos']:
                            print(f" - {correo}")
                    else:
                        print("No tiene correos electrónicos.")
            else:
                print("La agenda está vacía.")
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Implementacion
agenda_contactos()
