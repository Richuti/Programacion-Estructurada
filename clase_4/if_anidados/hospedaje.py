import os

def descuentoHospedaje():
    os.system("cls")
    temporada = input("Ingrese la temporada (alta/baja): ")
    noches = int(input("Ingrese la cantidad de noches: "))

    if temporada == "baja":
        if noches >= 3:
            print("Tiene 20% de descuento en su hospedaje")
        else:
            print("Tiene 10% de descuento en su hospedaje")
    else:
        if noches >= 5:
            print("Tiene 5% de descuento en su hospedaje")
        else:
            print("No aplica descuento en temporada alta")

if __name__ == "__main__":
    descuentoHospedaje()
