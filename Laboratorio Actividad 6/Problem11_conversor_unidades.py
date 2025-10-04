# conversor_unidades.py

class ConversorUnidades:
    def metros_a_pies(self, metros):
        """Convierte metros a pies."""
        return metros * 3.281

    def kilogramos_a_libras(self, kilogramos):
        """Convierte kilogramos a libras."""
        return kilogramos * 2.205

    def celsius_a_fahrenheit(self, celsius):
        """Convierte grados Celsius a grados Fahrenheit."""
        return (celsius * 9/5) + 32

    def litros_a_galones(self, litros):
        """Convierte litros a galones."""
        return litros * 0.264172

    def metros_cuadrados_a_pies_cuadrados(self, metros_cuadrados):
        """Convierte metros cuadrados a pies cuadrados."""
        return metros_cuadrados * 10.764

    def kilómetros_a_millas(self, kilometros):
        """Convierte kilómetros a millas."""
        return kilometros * 0.621371
