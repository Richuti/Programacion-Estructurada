palabra = input("Ingrese la palabra a buscar: ")
encontradas = 0
with open("servicios.txt", "r") as archivo:
    for linea in archivo:
        if palabra.lower() in linea.lower():
            print(linea.strip())
            encontradas += 1
print("Líneas encontradas:", encontradas)
