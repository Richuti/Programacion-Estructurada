import os

def calcular_comision(ventas, porcentaje):
    return ventas * porcentaje / 100


def probar_comision():
    os.system("cls")
    print("RETO 1: Comision de ventas")
    print("La funcion recibe ventas y porcentaje, y devuelve la comision.")
    print()

    print("Prueba 1 -> ventas 10000, 5%:", calcular_comision(10000, 5))
    print("Prueba 2 -> ventas 25000, 8%:", calcular_comision(25000, 8))
    print("Prueba 3 -> ventas 0, 10%:", calcular_comision(0, 10))

if __name__ == "__main__":
    probar_comision()
