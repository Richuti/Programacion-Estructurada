palabra = input("Ingrese una palabra: ")
normalizada = palabra.lower().replace(" ", "")
invertida = normalizada[::-1]
if normalizada == invertida:
    print(palabra, "es un palíndromo")
else:
    print(palabra, "no es un palíndromo")
