# main.py
from Problem11_conversor_unidades import ConversorUnidades

if __name__ == "__main__":
    conversor = ConversorUnidades()

    # Ejemplos
    metros = 10
    print(f"{metros} metros son {conversor.metros_a_pies(metros):.2f} pies")

    kilos = 70
    print(f"{kilos} kilogramos son {conversor.kilogramos_a_libras(kilos):.2f} libras")

    celsius = 25
    print(f"{celsius} °C son {conversor.celsius_a_fahrenheit(celsius):.2f} °F")

    litros = 5
    print(f"{litros} litros son {conversor.litros_a_galones(litros):.2f} galones")

    area_m2 = 50
    print(f"{area_m2} m² son {conversor.metros_cuadrados_a_pies_cuadrados(area_m2):.2f} ft²")

    km = 100
    print(f"{km} km son {conversor.kilómetros_a_millas(km):.2f} millas")
