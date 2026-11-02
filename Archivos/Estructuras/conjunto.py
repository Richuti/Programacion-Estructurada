identificadores = []
with open("identificadores.txt", "r") as archivo:
    for linea in archivo:
        identificador = linea.strip()
        if identificador != "":
            identificadores.append(identificador)
unicos = set(identificadores)
print("Leídos:", len(identificadores))
print("Únicos:", len(unicos))
print(sorted(unicos))
