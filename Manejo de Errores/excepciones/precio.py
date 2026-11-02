import os

def precioProducto():
    os.system("cls")

    try:
        precio = float(input("Ingrese el precio del producto: "))
        print(f"El precio del producto es: {precio}")
    except ValueError:
        print("Error: el precio debe ser un valor numerico")

if __name__ == "__main__":
    precioProducto()
