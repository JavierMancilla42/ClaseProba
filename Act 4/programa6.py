print("Programa para calcular sel interes compuesto")

#input
p = float(input("Capital principal sobre el cual se calcularán los intereses: "))
r = float(input("Tasa de interes: "))
r=r/100
t = float(input("Tiempo en el que se aplicará el interes: "))

#calculos
a=p*((1+r)**t)

print("El interes compuesto es", a)