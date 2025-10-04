# vector_3d.py
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def suma(self, vector2):
        """Realiza la suma de dos vectores."""
        return Vector3D(self.x + vector2.x, self.y + vector2.y, self.z + vector2.z)

    def resta(self, vector2):
        """Realiza la resta de dos vectores."""
        return Vector3D(self.x - vector2.x, self.y - vector2.y, self.z - vector2.z)

    def producto_escalar(self, vector2):
        """Calcula el producto escalar de dos vectores."""
        return self.x * vector2.x + self.y * vector2.y + self.z * vector2.z

    def modulo(self):
        """Calcula el módulo (longitud) del vector."""
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def normalizar(self):
        """Normaliza el vector (lo convierte en un vector unitario)."""
        modulo = self.modulo()
        return Vector3D(self.x / modulo, self.y / modulo, self.z / modulo)
