def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    invertida = ""
    for caracter in cadena:
        invertida = caracter + invertida

    return cadena == invertida

print(es_palindromo("Anita lava la tina"))