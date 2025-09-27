def diccionario_sinonimos():
    # Diccionario con algunos sinonimos de la lengua de Cervantes
    sinonimos = {
        "feliz": ["contento", "alegre", "satisfecho"],
        "triste": ["melancólico", "deprimido", "afligido"],
        "rápido": ["veloz", "ligero", "ágil"],
        "inteligente": ["listo", "sabio", "brillante"],
        "bonito": ["hermoso", "bello", "atractivo"]
    }

    while True:
        palabra = input("Escribe una palabra para ver sus sinónimos (o 'salir' para terminar): ").lower()
        if palabra == "salir":
            break
        elif palabra in sinonimos:
            print(f"Sinónimos de '{palabra}': {', '.join(sinonimos[palabra])}")
        else:
            print(f"No se encontraron sinónimos para '{palabra}'.")

    # Mostrar claves
    print("Palabras disponibles en el diccionario:")
    for clave in sinonimos.keys():
        print(clave)

# Implementacion
diccionario_sinonimos()
