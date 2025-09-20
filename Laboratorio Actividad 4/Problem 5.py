def cifrado_cesar(texto, desplazamiento):
    resultado = ""

    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            nuevo_codigo = (ord(caracter) - base + desplazamiento) % 26 + base
            resultado += chr(nuevo_codigo)
        else:
            resultado += caracter

    return resultado

# Ejemplo
mensaje = input("Ingresa el texto a cifrar: ")
desplazamiento = int(input("Ingresa el desplazamiento (puede ser negativo): "))
texto_cifrado = cifrado_cesar(mensaje, desplazamiento)
print("Texto cifrado:", texto_cifrado)
