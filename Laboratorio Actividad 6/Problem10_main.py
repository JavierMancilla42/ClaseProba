# main.py
from Problem10_vector_3d import Vector3D

if __name__ == "__main__":
    # Crea vectores
    v1 = Vector3D(3, 4, 5)
    v2 = Vector3D(1, 2, 3)

    # Suma
    suma = v1.suma(v2)
    print(f"Suma de vectores: ({suma.x}, {suma.y}, {suma.z})")

    # Resta
    resta = v1.resta(v2)
    print(f"Resta de vectores: ({resta.x}, {resta.y}, {resta.z})")

    # Producto punto
    producto = v1.producto_escalar(v2)
    print(f"Producto escalar: {producto}")

    # Módulo de v1
    print(f"Módulo de v1: {v1.modulo()}")

    # Normalización de v1
    normalizado = v1.normalizar()
    print(f"Vector normalizado v1: ({normalizado.x}, {normalizado.y}, {normalizado.z})")
