vacias = []
with open("registros.txt", "r") as archivo:
    for numero, linea in enumerate(archivo, 1):
        if linea.strip() == "":
            vacias.append(numero)
            print("Línea vacía:", numero)
print("Total de líneas vacías:", len(vacias))
