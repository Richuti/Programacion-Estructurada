import os

def cantidadProductos():
    os.system("cls")

    try:
        cantidad = int(input("Ingrese la cantidad de unidades a comprar: "))
        print(f"La cantidad de unidades es: {cantidad}")
    except ValueError:
        print("Error: la cantidad debe ser un numero entero")

if __name__ == "__main__":
    cantidadProductos()
