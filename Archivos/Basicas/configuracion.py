with open("configuracion.txt", "w") as archivo:
    archivo.write("host=localhost\n")
    archivo.write("puerto=1433\n")
    archivo.write("bd=ventas\n")
    archivo.write("usuario=admin\n")
    archivo.write("idioma=es\n")
print("Archivo configuracion.txt creado")
with open("configuracion.txt", "r") as archivo:
    print(archivo.read())
