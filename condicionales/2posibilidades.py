valor_ingresado = int(input("Por favor, ingrese un valor: "))

if valor_ingresado > 0:
    print("El valor es positivo")
elif valor_ingresado < 0:
    print("El valor es negativo")
else:
    print("El valor es cero")

if valor_ingresado % 5 == 0:
    print("El valor es divisible por 5")
