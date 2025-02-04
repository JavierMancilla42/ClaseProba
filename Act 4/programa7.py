print("Programa para calcular si un numero par o impar")

#input
n = float(input("Qué numero desea calcular?: "))
n2=n

#Calculo
v=n%2

#If
if v==0:
  print("El numero", n, "es par")
else:
  print("El numero", n, "es impar")

#ciclo
i=2
d=[1]
while n>i:
  v=n2%i
  if v==0:
   d.append(i)
   n2=n2/i
  else:
   i=i+1

      
print("y sufactores son:")
print(d)
