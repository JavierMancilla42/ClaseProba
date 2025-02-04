print("Programa para calcular si un numero es primo")

#input
p = float(input("Qué numero desea calcular?: "))

#inicializacion de variables
n=2
r=0

#Ciclo
while p-1>n:
  r=p%n
  if r==0:
   print("El numero no es primo")
  else:
   print("El numero es primo")
  n=n+1