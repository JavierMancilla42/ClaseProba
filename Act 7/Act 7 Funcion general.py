import math as mt

#Definicion de funcion
def cuadratica (a,b,c):
    
    #Definicion de discriminante
    d = (b**2)-(4*a*c)

    if d > 0:
        t="Las raices son reales y diferentes"
        x1 = (-b + mt.sqrt(d))/(2*a)
        x2 = (-b - mt.sqrt(d))/(2*a)
    elif d == 0:
        t="Las raices son reales e iguales"
        x1 = (-b + mt.sqrt(d))/(2*a)
        x2 = (-b - mt.sqrt(d))/(2*a)
    else:
        t="Las raices son complejas"
        x1 = (-b + 1j*mt.sqrt(d))/(2*a)
        x2 = (-b - 1j*mt.sqrt(d))/(2*a)
    return t, x1, x2

#Inicio del input
print("Este programa resuelve ecuaciones de segundo grado dados sus coeficientes")
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

t, x1, x2 = cuadratica(a,b,c)

print(t)
print(x1)
print(x2)