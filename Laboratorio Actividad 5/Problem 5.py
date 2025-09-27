def diccionario_precios():
    precios = {
        "pan": 15,
        "leche": 33,
        "arroz": 30,
        "huevo": 5,
        "azúcar": 25
    }

    while True:
        print("\nMenú:")
        print("1. Consultar precio de un producto")
        print("2. Agregar o actualizar un producto")
        print("3. Ver todos los productos")
        print("4. Salir")

        opcion = input("Elige una opción (1-4): ")

        #Switch
        if opcion == "1":
            producto = input("Ingresa el nombre del producto: ").lower()
            if producto in precios:
                print(f"El precio de '{producto}' es: ${precios[producto]:.2f}")
            else:
                print(f"El producto '{producto}' no está en la lista.")

        elif opcion == "2":
            producto = input("Nombre del producto a agregar o actualizar: ").lower()
            try:
                precio = float(input(f"Ingrese el precio de '{producto}': "))
                precios[producto] = precio
                print(f"Producto '{producto}' guardado con precio ${precio:.2f}")
            except ValueError:
                print("El precio debe ser un número válido.")

        elif opcion == "3":
            if precios:
                print("\nLista de productos y precios:")
                for producto, precio in precios.items():
                    print(f"{producto}: ${precio:.2f}")
            else:
                print("La lista de productos está vacía.")

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

# Implementacion
diccionario_precios()
