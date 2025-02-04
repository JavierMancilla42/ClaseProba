#Instrucciones basicas
print("Esta es una calculadora para operaciones binarias simples")
print("presione [s] para suma")
print("presione [r] para resta")
print("presione [m] para multiplicacion")
print("presione [d] para division")

#validacion del input

v="e"
while v!="s" and v!="r" and v!="m" and v!="d":
    v= input("Especifique el tipo de operacion para realizar: ")
    print(v)
    if v!="s" and v!="r" and v!="m" and v!="d":
      print("caracter no valido")

#lectura de numeros 
x1= float(input("Especifique el primer numero a operar: "))
x2= float(input("Especifique el segundo numero a operar: "))

#Seleccion de operacion
if v=="s":
   x=x1+x2
   print("la suma es: ", x)
elif v=="r":
   x=x1-x2
   print("la resta es: ", x)
elif v=="m":
   x=x1*x2
   print("la multiplicacion es: ", x)
elif v=="d":
   x=x1/x2
   print("la division es: ", x)
else:
   print("error")
