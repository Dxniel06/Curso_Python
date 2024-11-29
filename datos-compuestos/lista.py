elementos_lista = [42, "Python", False, 3.14]
print(elementos_lista[0])
print(type(elementos_lista[0]))
print(type(elementos_lista[1]))
print(type(elementos_lista[2]))
print(type(elementos_lista[3]))

elementos_lista[1] = 100
print(type(elementos_lista[1]))

if type(elementos_lista[1]) == int:
    print("El elemento en el índice 1 ahora es un número entero")
else:
    print("El elemento en el índice 1 no es un número entero")
