print("Programa para calcular una seccuencia de fibonacci")

#input
n = float(input("Cuántos terminos de la seccuencia desea calcular?: "))
n=n-1

#inicializacion de variables
f=[0,1]
i=0

print(f[i])

#Ciclo
while n>i:
  i=i+1
  print(f[i])
  f.append(f[i]+f[i-1])