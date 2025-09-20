def invertir_palabras(frase):
    palabras = frase.split()  # Separar
    palabras_invertidas = [palabra[::-1] for palabra in palabras]  # Inviertir
    frase_invertida = ' '.join(palabras_invertidas)  # Unir
    return frase_invertida

# Ejemplo
frase_original = input("Ingresa una frase: ")
frase_resultado = invertir_palabras(frase_original)
print("Frase con palabras invertidas:", frase_resultado)

