from collections import Counter

def calcular_moda(numeros):
    if not numeros:
        return None

    contador = Counter(numeros)
    
    max_frecuencia = max(contador.values())
   
    modas = [numero for numero, frecuencia in contador.items() if frecuencia == max_frecuencia]

    if len(modas) == 1:
        return modas[0]  
    return modas 

print(calcular_moda([1, 2, 3, 4, 4, 5]))