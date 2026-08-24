import os
os.system("cls")

zona = input("Ingrese la zona (urbana/rural): ")
peso = float(input("Ingrese el peso del paquete en kg: "))

if zona == "urbana":
    if peso <= 5:
        tarifa = 50
    else:
        tarifa = 80
else:
    if peso <= 5:
        tarifa = 90
    else:
        tarifa = 130

print(f"La tarifa de entrega es {tarifa} cordobas")
