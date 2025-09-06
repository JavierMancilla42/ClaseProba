def invertir_cadena(texto):
    invertida = ""
    for caracter in texto:
        invertida = caracter + invertida
    return invertida
    
cadena = "Hola mundo"
cadena_invertida = invertir_cadena(cadena)
print(cadena_invertida)