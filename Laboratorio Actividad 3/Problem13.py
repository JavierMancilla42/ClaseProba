def es_bisiesto(anio):
    # Un año es bisiesto si es divisible por 4, pero no divisible por 100, excepto si es divisible por 400.
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

print(es_bisiesto(2020)) 