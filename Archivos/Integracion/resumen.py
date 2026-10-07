registros = []
activos = 0
with open("equipos.txt", "r") as archivo:
    for linea in archivo:
        registro = linea.strip()
        if registro != "":
            registros.append(registro)
            if registro.endswith("Activo"):
                activos += 1
unicos = set(registros)
with open("resumen.txt", "w") as archivo:
    archivo.write("Cantidad de registros: " + str(len(registros)) + "\n")
    archivo.write("Registros activos: " + str(activos) + "\n")
    archivo.write("Registros unicos: " + str(len(unicos)) + "\n")
print("Archivo resumen.txt generado")
with open("resumen.txt", "r") as archivo:
    print(archivo.read())
