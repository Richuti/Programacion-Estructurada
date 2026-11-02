registros = []
servicios = set()
estados = {}
activos = []
with open("registros.txt", "r") as archivo:
    for linea in archivo:
        linea_limpia = linea.strip()
        if linea_limpia != "":
            codigo, servicio, estado = linea_limpia.split("|")
            registros.append([codigo, servicio, estado])
            servicios.add(servicio)
            estados[estado] = estados.get(estado, 0) + 1
            if estado == "Activo":
                activos.append(codigo + " - " + servicio)
with open("reporte.txt", "w") as archivo:
    archivo.write("REPORTE DE REGISTROS\n")
    archivo.write("Total de registros: " + str(len(registros)) + "\n")
    archivo.write("Servicios distintos: " + str(len(servicios)) + "\n")
    archivo.write("Registros por estado:\n")
    for estado, cantidad in estados.items():
        archivo.write("  " + estado + ": " + str(cantidad) + "\n")
    archivo.write("Registros activos:\n")
    for registro in activos:
        archivo.write("  " + registro + "\n")
print("Archivo reporte.txt generado")
with open("reporte.txt", "r") as archivo:
    print(archivo.read())
