frecuencias = {}
with open("palabras.txt", "r") as archivo:
    for linea in archivo:
        for palabra in linea.lower().split():
            frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
print(frecuencias)
for palabra, veces in frecuencias.items():
    print(palabra, ":", veces)
