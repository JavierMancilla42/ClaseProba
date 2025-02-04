print("Programa para calcular el factorial de un numero")

#input
n = float(input("Ingrese el numero: "))
n2=n

#Ciclo
n1=n
while n>1:
  n=n-1
  n1=n1*n

#output
print("El factorial de", n2, "es", n1)