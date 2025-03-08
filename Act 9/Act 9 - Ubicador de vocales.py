#Definicion de funcion
def ubicadorDeVocales(cadena):
    vocales = "aeiouáéíóúü"
    ubicaciones = {}
    cadena = cadena.lower()
    
    for index, char in enumerate(cadena):
        if char in vocales:
            if char in ubicaciones:
                ubicaciones[char].append(index)
            else:
                ubicaciones[char] = [index]
    
    return ubicaciones

#Inicio del input
texto = input("Ingrese una cadena de texto: ")
resultado = ubicadorDeVocales(texto)
print("Ubicación de vocales:", resultado)