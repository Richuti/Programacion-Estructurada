nombre = input("Ingrese el nombre del archivo: ")
if nombre.endswith(".csv"):
    print("El archivo termina en .csv")
else:
    print("El archivo no termina en .csv")
if nombre.startswith("reporte"):
    print("El archivo comienza con reporte")
else:
    print("El archivo no comienza con reporte")
