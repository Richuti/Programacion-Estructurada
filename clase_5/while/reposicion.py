import os

def reposicionInventario():
    os.system("cls")
    existencia = 0

    while existencia < 20:
        cantidad = int(input("Ingrese la cantidad a reponer: "))
        if cantidad > 0:
            existencia = existencia + cantidad
            print(f"Existencia actual: {existencia}")
        else:
            print("La cantidad debe ser mayor que cero")

    print(f"Se alcanzo la meta con {existencia} unidades")

if __name__ == "__main__":
    reposicionInventario()
