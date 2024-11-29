cadena = "Python"
cadena2 = cadena.lower()
print(dir(cadena))
print(cadena)
print(cadena2.capitalize())

cadena_larga = "Bienvenidos al curso de Python, vamos a aprender juntos"

print(cadena_larga.find("Python"))
print(cadena_larga.find("java"))
try:
    print(cadena_larga.index("java"))
except ValueError:
    print("El término 'java' no se encuentra en la cadena.")

print(cadena.isalpha())
print(cadena.isnumeric())
print(cadena_larga.count("o"))
print(len(cadena_larga))
print(cadena_larga.split(" "))
