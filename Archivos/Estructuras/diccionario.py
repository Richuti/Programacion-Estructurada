configuracion = {}
with open("configuracion.txt", "r") as archivo:
    for linea in archivo:
        linea_limpia = linea.strip()
        if linea_limpia != "":
            clave, valor = linea_limpia.split("=", 1)
            configuracion[clave] = valor
print(configuracion)
for clave, valor in configuracion.items():
    print(clave, ":", valor)
