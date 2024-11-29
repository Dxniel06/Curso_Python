nombre_usuario = "Daniel"
edad_usuario = 18

print(nombre_usuario)
print(edad_usuario)

nombre_usuario = 11
edad_usuario = "Fernanda"

print(nombre_usuario)
print(edad_usuario)

if isinstance(nombre_usuario, str):
    print("El nombre es ahora una cadena de texto")
else:
    print("El nombre ya no es una cadena de texto")

if isinstance(edad_usuario, int):
    print("La edad es ahora un número entero")
else:
    print("La edad ya no es un número entero")
