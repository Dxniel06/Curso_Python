tupla_datos = (42, "Mundo", False, 3.1416)

print(type(tupla_datos[0]))
print(type(tupla_datos[1]))
print(type(tupla_datos[2]))
print(type(tupla_datos[3]))

print(tupla_datos)

if type(tupla_datos[0]) == int:
    print("El primer elemento es un número entero")
else:
    print("El primer elemento no es un número entero")
