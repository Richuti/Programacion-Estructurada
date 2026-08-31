import os

def calculoComision():
    os.system("cls")

    # Se espera un ValueError si el usuario escribe texto en lugar de numeros
    try:
        ventas = float(input("Ingrese el total de ventas: "))
        porcentaje = float(input("Ingrese el porcentaje de comision: "))

        comision = ventas * (porcentaje / 100)

        print(f"La comision es: {comision}")
    except ValueError:
        print("Error: las ventas y el porcentaje deben ser valores numericos")

if __name__ == "__main__":
    calculoComision()
