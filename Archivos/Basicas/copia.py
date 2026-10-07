with open("texto.txt", "r") as origen:
    contenido = origen.read()
with open("texto_copia.txt", "w") as copia:
    copia.write(contenido)
print("Copia creada: texto_copia.txt")
print(contenido)
