import math

def ordenar_puntos_por_distancia(puntos):
    # Calcular norma
    def distancia_al_origen(punto):
        x, y = punto
        return math.sqrt(x**2 + y**2)
    
    # Ordenar
    puntos_ordenados = sorted(puntos, key=distancia_al_origen)
    return puntos_ordenados

# Implementacion
lista_puntos = [(3, 4), (1, 1), (0, 0), (2, 2), (5, 0)] #Lista a ordenar
puntos_ordenados = ordenar_puntos_por_distancia(lista_puntos)
print("Puntos ordenados por distancia al origen:")
print(puntos_ordenados)
