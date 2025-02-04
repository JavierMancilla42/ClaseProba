print("Programa para generar una lista de numeros pares e impares")

#input
n = float(input("Hasta que numero desea generar la lista?: "))
n=n-1

#declaracion de variable
v=0

#Ciclo para pares
print("Los numeros pares hasta ", n+1, " son:")
while v<n:
  v=v+2
  print(v)

print("")
print("")

#Ciclo para impares
v=1
print("Los numeros impares hasta ", n+1, " son:")
while v<n:
  v=v+2
  print(v)

