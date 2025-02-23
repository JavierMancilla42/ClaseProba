def suma_serie_numerica(numeros):
    return sum(numeros)
    
print("Calculadora de suma de una serie numérica")   #instrucciones
numeros = input("Ingrese los números separados por espacios: ")    
lista_numeros = [float(num) for num in numeros.split()]    #Split de la cadena de texto y conversion de tipo de variable
print("La suma de la serie es:", suma_serie_numerica(lista_numeros))   #Output