numero_repeticiones = 5
for contador_actual in range(numero_repeticiones):
    if contador_actual == numero_repeticiones - 1:
        print(f"¡Este es el adiós final! Iteración número {contador_actual + 1}")
    elif contador_actual == 0:
        print(f"¡Comenzamos! Iteración número {contador_actual + 1}")
    elif contador_actual == 1:
        print(f"Ya estamos en el segundo paso. Iteración número {contador_actual + 1}")
    elif contador_actual == 2:
        print(f"Mitad del camino recorrido. Iteración número {contador_actual + 1}")
    elif contador_actual == 3:
        print(f"Casi terminamos. Iteración número {contador_actual + 1}")
