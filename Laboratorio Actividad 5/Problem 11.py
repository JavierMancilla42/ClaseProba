def registro_compras():
    compras = []

    while True:
        print("\nMenú:")
        print("1. Agregar compra")
        print("2. Mostrar total gastado")
        print("3. Salir")

        opcion = input("Elige una opción (1-3): ")

        if opcion == "1":
            producto = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio_unitario = float(input("Precio unitario: "))
            except ValueError:
                print("Cantidad debe ser un entero y precio un número válido.")
                continue

            compra = (producto, cantidad, precio_unitario)
            compras.append(compra)
            print(f"Compra de {cantidad} '{producto}' agregada.")

        elif opcion == "2":
            if compras:
                total = sum(cantidad * precio for _, cantidad, precio in compras)
                print(f"Total gastado: ${total:.2f}")
            else:
                print("No hay compras registradas.")

        elif opcion == "3":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

# Implementacion
registro_compras()
