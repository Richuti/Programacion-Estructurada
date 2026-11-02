registros = []
with open("registros.txt", "r") as archivo:
    for linea in archivo:
        linea_limpia = linea.strip()
        if linea_limpia != "":
            campos = linea_limpia.split("|")
            registros.append(campos)
for campos in registros:
    print(campos)
print("Total de registros:", len(registros))
