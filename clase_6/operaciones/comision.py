import os

def calculoComision():
    os.system("cls")

    try:
        ventas = float(input("Ingrese el total de ventas: "))
        porcentaje = float(input("Ingrese el porcentaje de comision: "))

        comision = ventas * (porcentaje / 100)

        print(f"La comision es: {comision}")
    except ValueError:
        print("Error: las ventas y el porcentaje deben ser valores numericos")

if __name__ == "__main__":
    calculoComision()
