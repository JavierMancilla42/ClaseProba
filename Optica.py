#Programa optica
import numpy as np
import math as mt
import mpmath as mp
import matplotlib.pyplot as plt

#Parametros###########################
#radios de curvatura de la lente
r1 = 10
r2 = 6

#distancia de separacion o grosor de la lente
d1 = 3.7

#Indices de refraccion del medio y la lente
n0 = 1
n1 = 1.45

#Centro de curvatura o posicion del segundo circulo
h2 = -6

#Origen de la luz
x1 = -30
y1 = 0

#Cantidad de rayos a graficar
s1 = 10

#Apertura de la lente
ap = 4.2







#Variables############################
#Centro de curvatura del primer circulo, no editar
h1 = h2 + r2 - d1 + r1

#Cantidad de rayos a graficar

t0 = mt.atan(((y1+0.5*ap)/(x1-(h2+r2-d1))))*180/np.pi

#Angulo final
tf = mt.atan(((y1-0.5*ap)/(x1-(h2+r2-d1))))*180/np.pi

#Tamaño angular
ta = tf-t0

#aumento de rayos
ts = (tf-t0)/s1

#lista de rayos
t1=[t0]

s=1
while s < s1+1:
  t1.append(t0+(s*ts))
  s += 1













#Funciones############################
#Interseccion en x de la recta y circunferencia
def F3(x,y,m,h,k,r,s):
    f3 = ((-1*( (-2*h -2*m**2*x +2*m*y -2*k*m)) + s*np.sqrt( ( (-2*h -2*m**2*x +2*m*y -2*k*m)**2) -4*(1+m**2)*(h**2 +m**2*x**2 +y**2 -2*m*x*y +2*k*m*x -2*k*y +k**2 -r**2) ) )) / 2*(1+m**2)
    return f3

#Ley de snell despejada
def F4(ni,nf,ti):
    f4 = mt.asin( (ni*mt.sin(ti*np.pi/180)) /nf )*180/np.pi
    return f4





#Raytracing###########################

x2=[]
y2=[]
tn1=[]
t2=[]
x3=[]
y3=[]
tn2=[]
t3=[]
x4=[]
y4=0

i=0
while i < s1+1:

  #Coordenadas del punto de incidencia del haz de luz con la primera circunferencia

  x2.append(F3(x1, y1, np.tan(t1[i]*np.pi/180), h1, 0, r1, -1))
  y2.append((x2[i]-x1)*np.tan(t1[i]*np.pi/180) + y1)

  #angulo de la recta normal al primer circulo en el punto de incidencia 1

  tn1.append(mt.atan(y2[i]/(x2[i]-h1))*180/np.pi)

  #angulo de la recta de salida

  t2.append(F4(n0, n1, t1[i]-tn1[i])+tn1[i])

  #Coordenadas del punto de incidencia del haz de luz con la segunda circunferencia

  x3.append(F3(x2[i], y2[i], np.tan(t2[i]*np.pi/180), h2, 0, r2, 1))
  y3.append((x3[i]-x2[i])*np.tan(t2[i]*np.pi/180) + y2[i])

  #angulo de la normal del segundo circulo en el punto x3

  tn2.append(mt.atan(y3[i]/(x3[i]-h2))*180/np.pi)

  #angulo de la recta de salida

  t3.append(F4(n1, n0, -1*tn2[i] + t2[i])+tn2[i])

  x4.append((-1*y3[i]+x3[i]*np.tan(t3[i]*np.pi/180))/(np.tan(t3[i]*np.pi/180)))

  i += 1






#Renderizado##########################

print("Simulación con" ,s, "rayos")
print("Datos de la lente: Radios r1:",r1,", r2:", r2, " y grosor:", d1)
print("La luz esta saliendo desde el punto (", x1,",",y1,")")

i=0
while i < s1+1:
  plt.axline((x1, y1), (x2[i],y2[i]),color=('r'))
  #plt.axline((x2[i], y2[i]), (x3[i],y3[i]), color=('g'))
  plt.axline((x3[i], y3[i]), (x4[i],y4), color=('g'))
  i += 1

circle1 = plt.Circle((h1, 0), r1, color='b', fill=False)
circle2 = plt.Circle((h2, 0), r2, color='b', fill=False)

ax = plt.gca()

ax.add_patch(circle1)
ax.add_patch(circle2)

ax.set_xlim((-7, 13)) #Se puede editar para cambiar el área de interes
ax.set_ylim((-7.5, 7.5)) #Se puede editar para cambiar el área de interes
plt.title("Simulacion con raycing")
plt.grid()

# aspect ratio 4:3

plt.draw()