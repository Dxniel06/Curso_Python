numero = int(input("Introduce un número: "))
if numero > 15:
    print("El número es mayor que 15.")
    if numero > 25:
        print("Además, es mayor que 25.")
elif numero > 10:
    print("Está entre 11 y 15.")

if numero % 4 == 0:
    print("El número es divisible por 4.")
