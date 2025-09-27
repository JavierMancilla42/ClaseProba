def registro_ventas():
    ventas = []

    while True:
        print("\nMenú:")
        print("1. Agregar venta")
        print("2. Mostrar todas las ventas")
        print("3. Mostrar total vendido por producto")
        print("4. Salir")

        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            producto = input("Nombre del producto: ").strip()
            mes = input("Mes de la venta: ").strip()
            try:
                cantidad = int(input("Cantidad vendida: "))
            except ValueError:
                print("Cantidad inválida. Debe ser un número entero.")
                continue

            venta = {
                "producto": producto,
                "mes": mes,
                "cantidad_vendida": cantidad
            }
            ventas.append(venta)
            print(f"Venta registrada: {cantidad} unidades de '{producto}' en {mes}.")

        elif opcion == "2":
            if ventas:
                print("\nVentas registradas:")
                for i, v in enumerate(ventas, start=1):
                    print(f"{i}. Producto: {v['producto']}, Mes: {v['mes']}, Cantidad vendida: {v['cantidad_vendida']}")
            else:
                print("No hay ventas registradas.")

        elif opcion == "3":
            if ventas:
                total_por_producto = {}
                for venta in ventas:
                    prod = venta["producto"]
                    total_por_producto[prod] = total_por_producto.get(prod, 0) + venta["cantidad_vendida"]

                print("\nTotal vendido por producto:")
                for prod, total in total_por_producto.items():
                    print(f"{prod}: {total} unidades")
            else:
                print("No hay ventas registradas.")

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

# Implementacion
registro_ventas()
