with open("archivos.txt", "r") as archivo:
    for linea in archivo:
        nombre = linea.strip()
        if nombre.lower().endswith(".csv"):
            print(nombre)
