import os

def promedioVentas():
    os.system("cls")

    try:
        venta1 = float(input("Ingrese la venta 1: "))
        venta2 = float(input("Ingrese la venta 2: "))
        venta3 = float(input("Ingrese la venta 3: "))

        cantidad_ventas = 3
        promedio = (venta1 + venta2 + venta3) / cantidad_ventas

        print(f"El promedio de las ventas es: {promedio}")
    except ValueError:
        print("Error: las ventas deben ser valores numericos")
    except ZeroDivisionError:
        print("Error: no se puede calcular el promedio sin datos")

if __name__ == "__main__":
    promedioVentas()
