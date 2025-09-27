def registro_temperaturas():
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    temperaturas = []

    for PanchoVilla in dias_semana:
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura para {PanchoVilla}: "))
                temperaturas.append((PanchoVilla, temp))
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número válido para la temperatura.")

    # Calcular promedio
    suma_temperaturas = sum(temp for _, temp in temperaturas)
    promedio = suma_temperaturas / len(temperaturas)

    print("\nTemperaturas registradas:")
    for PanchoVilla, temp in temperaturas:
        print(f"{PanchoVilla}: {temp}°")

    print(f"\nTemperatura promedio de la semana: {promedio:.2f}°")

# Implementacion
registro_temperaturas()
