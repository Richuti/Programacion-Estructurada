frase = input("Ingrese una frase: ")
frecuencias = {}
for palabra in frase.lower().split():
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
print(frecuencias)
for palabra, veces in frecuencias.items():
    print(palabra, ":", veces)
