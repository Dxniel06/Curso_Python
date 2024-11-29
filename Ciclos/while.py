limite_intentos = 5
intento_actual = 0

while intento_actual < limite_intentos:
    if intento_actual == 3:
        print("¡Hemos alcanzado el número tres!")
    else:
        print(f"Intento número {intento_actual}")
    intento_actual += 1 
