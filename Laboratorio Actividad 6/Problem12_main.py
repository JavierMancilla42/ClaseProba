# main.py
from Problem12_cifrador_cesar import CifradorCesar

if __name__ == "__main__":
    cifrador = CifradorCesar(desplazamiento=3)

    # Mensaje original
    mensaje = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
    print("Mensaje original:", mensaje)

    # Cifrado
    mensaje_cifrado = cifrador.cifrar(mensaje)
    print("Mensaje cifrado:", mensaje_cifrado)

    # Descifrado
    mensaje_descifrado = cifrador.descifrar(mensaje_cifrado)
    print("Mensaje descifrado:", mensaje_descifrado)
