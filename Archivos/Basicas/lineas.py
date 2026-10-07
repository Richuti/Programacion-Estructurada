lineas = 0
with open("equipos.txt", "r") as archivo:
    for linea in archivo:
        if linea.strip() != "":
            lineas += 1
print("Líneas con contenido:", lineas)
