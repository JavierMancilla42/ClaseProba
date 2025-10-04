# main.py
from Problem9_calculadora_cientifica import CalculadoraCientifica

if __name__ == "__main__":
    # Crear objeto de la clase
    calc = CalculadoraCientifica()

    # Probar algunos métodos
    numero = 16
    print(f"Raíz cuadrada de {numero}: {calc.calcular_raiz_cuadrada(numero)}")

    base = 10
    exponente = 3
    print(f"{base} elevado a {exponente}: {calc.calcular_potencia(base, exponente)}")

    valor = 100
    print(f"Logaritmo de {valor} en base 10: {calc.calcular_logaritmo(valor)}")

    angulo = 45
    print(f"Seno de {angulo}°: {calc.calcular_seno(angulo)}")
    print(f"Coseno de {angulo}°: {calc.calcular_coseno(angulo)}")
    print(f"Tangente de {angulo}°: {calc.calcular_tangente(angulo)}")

