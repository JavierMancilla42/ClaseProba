def registrar_puntajes():
    puntajes = {}

    while True:
        nombre = input("Ingresa el nombre del jugador (o escribe 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break

        try:
            puntaje = int(input(f"Ingrese el puntaje de {nombre}: "))
        except ValueError:
            print("El puntaje debe ser un número entero. Inténtalo de nuevo.")
            continue

        # Guardar
        puntajes[nombre] = puntaje

    # Imprimir
    print("Puntajes de jugadores:")
    for jugador, puntaje in puntajes.items():
        print(f"{jugador}: {puntaje}")

# Implementacion
registrar_puntajes()