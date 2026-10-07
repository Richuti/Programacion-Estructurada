with open("registro.txt", "a") as archivo:
    archivo.write("Firewall perimetral\n")
    archivo.write("Servidor de respaldos\n")
    archivo.write("Router de borde\n")
print("Se agregaron tres registros")
with open("registro.txt", "r") as archivo:
    print(archivo.read())
