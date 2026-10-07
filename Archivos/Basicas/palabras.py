total = 0
with open("texto.txt", "r") as archivo:
    for linea in archivo:
        palabras = linea.split()
        total += len(palabras)
print("Total de palabras:", total)
