import os

def tiposIncompatibles():
    os.system("cls")

    cantidad = input("Ingrese la cantidad de productos: ")

    try:
        total = cantidad + 10
        print(f"El total es: {total}")
    except TypeError:
        print("Ocurrio un TypeError porque input() devuelve una cadena")
        print("y Python no puede sumar una cadena con un numero entero.")

    try:
        total = int(cantidad) + 10
        print(f"Corregido, el total es: {total}")
    except ValueError:
        print("Error: la cantidad debe ser un numero entero")

if __name__ == "__main__":
    tiposIncompatibles()
