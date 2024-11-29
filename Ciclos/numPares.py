numero_ingresado = int(input("Ingrese un número: "))
limite_superior = numero_ingresado

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for contador_actual in range(limite_superior):
    if contador_actual % 5 == 0 and contador_actual != 0:
        print(f"El número {contador_actual} es múltiplo de 5")
    elif contador_actual % 3 == 0:
        print(f"El número {contador_actual} es múltiplo de 3")
    elif contador_actual % 2 == 0:
        print(f"El número {contador_actual} es par")
    elif es_primo(contador_actual):
        print(f"El número {contador_actual} es primo")
    else:
        print(f"El número {contador_actual} es impar")
