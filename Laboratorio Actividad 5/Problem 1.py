import string

def contar_palabras(texto):
    # Limpiar el texto
    texto = texto.lower()
    for caracter in string.punctuation:
        texto = texto.replace(caracter, "")
    
    # Separar
    palabras = texto.split()
    
    # Crear diccionario
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    # Imprimir
    print("Frecuencia de palabras:")
    for palabra, cantidad in frecuencia.items():
        print(f"{palabra}: {cantidad}")

# Implementacion
texto_usuario = input("Escribe un párrafo: ")
contar_palabras(texto_usuario)
