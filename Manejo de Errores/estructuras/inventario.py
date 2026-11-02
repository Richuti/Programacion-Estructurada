import os

def indiceInventario():
    os.system("cls")

    productos = ["Arroz", "Frijoles", "Aceite", "Azucar", "Sal"]

    print("Productos disponibles:")
    for producto in productos:
        print(f"- {producto}")

    try:
        posicion = int(input("Ingrese la posicion del producto: "))
        print(f"El producto en la posicion {posicion} es: {productos[posicion]}")
    except ValueError:
        print("Error de formato: la posicion debe ser un numero entero")
    except IndexError:
        print("Error de rango: esa posicion no existe en la lista")

if __name__ == "__main__":
    indiceInventario()
