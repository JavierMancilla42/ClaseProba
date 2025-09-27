#Definicion de diccionario 
datosClima = {
    'lat': 28.5421,
    'lon': -81.379,
    'timezone': 'America/New_York',
    'timezone_offset': -18000,
    'daily': [
        {'dt': '09/Sep/24', 'temp': 26.33, 'pressure': 1020, 'humidity': 58},
        {'dt': '10/Sep/24', 'temp': 28.03, 'pressure': 1018, 'humidity': 47},
        {'dt': '11/Sep/24', 'temp': 28.93, 'pressure': 1018, 'humidity': 56},
        {'dt': '12/Sep/24', 'temp': 30.8,  'pressure': 1018, 'humidity': 46},
        {'dt': '13/Sep/24', 'temp': 27.17, 'pressure': 1019, 'humidity': 61},
        {'dt': '14/Sep/24', 'temp': 24.02, 'pressure': 1020, 'humidity': 67},
        {'dt': '17/Sep/24', 'temp': 23.73, 'pressure': 1023, 'humidity': 40},
        {'dt': '18/Sep/24', 'temp': 24.7,  'pressure': 1024, 'humidity': 39}
    ]
}

#preguntas

#1. ¿Cómo puedo obtener la latitud y longitud del lugar registrado en datosClima?
latitud = datosClima['lat']
longitud = datosClima['lon']
print(f"Latitud: {latitud}, Longitud: {longitud}")


#2. ¿Imprimir el valor de la presión atmosférica el 11 de septiembre?
for dia in datosClima['daily']:
    if dia['dt'] == '11/Sep/24':
        print(f"Presión el 11 de septiembre: {dia['pressure']} hPa")
        break


#3. ¿Cuál es la humedad relativa el 13 de septiembre?
for dia in datosClima['daily']:
    if dia['dt'] == '13/Sep/24':
        print(f"Humedad el 13 de septiembre: {dia['humidity']}%")
        break


#4. ¿Cómo accedo a la lista completa de datos diarios (claves 'daily')?
lista_diaria = datosClima['daily']
print("Lista completa de datos diarios:")
print(lista_diaria)


#5. ¿Cómo obtengo la temperatura registrada el 14 de septiembre?
for dia in datosClima['daily']:
    if dia['dt'] == '14/Sep/24':
        print(f"Temperatura el 14 de septiembre: {dia['temp']} °C")
        break


#6. ¿Cuántos elementos hay en la lista 'daily'?
cantidad_dias = len(datosClima['daily'])
print(f"Cantidad de días registrados en 'daily': {cantidad_dias}")
