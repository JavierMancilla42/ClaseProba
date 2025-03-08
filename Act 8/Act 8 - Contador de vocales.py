#Definicion de funcion
def contadorDeVocales(cadena):
    vocales = "aeiouáéíóúü"
    conteo_vocales = {}
    cadena = cadena.lower()
    
    #Loop para recorrer cada caracter en cadena
    for char in cadena:
        if char in vocales:    #Si el caracter es una vocal
            if char in conteo_vocales:  #Si el caracter ya esta en el diccionario
                conteo_vocales[char] += 1
            else:     #si no esta
                conteo_vocales[char] = 1
    
    return conteo_vocales

#Inicio del input
texto = input("Ingrese una cadena de texto: ")
resultado = contadorDeVocales(texto)
print("Conteo de vocales:", resultado)