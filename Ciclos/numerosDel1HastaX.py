numero = int(input("Ingrese un número: "))
limite = numero

for i in range(limite):
    if (i + 1) % 2 == 0:
        print(f"{i + 1} es un número par")
    else:
        print(i + 1)
