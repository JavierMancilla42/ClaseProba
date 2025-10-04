# calculadora_cientifica.py
import math

class CalculadoraCientifica:
    def calcular_raiz_cuadrada(self, numero):
        #Calcula la raíz cuadrada de un número.
        return math.sqrt(numero)

    def calcular_logaritmo(self, numero, base=10):
        #Calcula el logaritmo de un número en la base especificada 
        #(por defecto, base 10)
        return math.log(numero, base)

    def calcular_potencia(self, base, exponente):
        #Calcula la potencia de un número dado una base y un exponente.
        return base ** exponente

    def calcular_seno(self, angulo_grados):
        #Calcula el seno de un ángulo en grados.
        angulo_radianes = math.radians(angulo_grados)
        return math.sin(angulo_radianes)

    def calcular_coseno(self, angulo_grados):
        #Calcula el coseno de un ángulo en grados.
        angulo_radianes = math.radians(angulo_grados)
        return math.cos(angulo_radianes)

    def calcular_tangente(self, angulo_grados):
        #Calcula la tangente de un ángulo en grados.
        angulo_radianes = math.radians(angulo_grados)
        return math.tan(angulo_radianes)
