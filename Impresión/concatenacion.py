saludo = "Buenos días"
sustantivo = "Amigos"
mensaje_concatenado = saludo + " " + sustantivo

print(saludo)
print(sustantivo)
print(mensaje_concatenado)

if " " in mensaje_concatenado:
    print("La cadena concatenada tiene un espacio entre las palabras")
else:
    print("La cadena concatenada no tiene un espacio entre las palabras")
