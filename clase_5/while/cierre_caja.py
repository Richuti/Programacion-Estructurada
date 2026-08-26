import os

def cierreCaja():
    os.system("cls")
    total = 0
    cantidad = 0

    venta = float(input("Ingrese una venta (0 para terminar): "))

    while venta != 0:
        total = total + venta
        cantidad = cantidad + 1
        venta = float(input("Ingrese una venta (0 para terminar): "))

    print(f"Se registraron {cantidad} ventas")
    print(f"El total del dia es {total}")

if __name__ == "__main__":
    cierreCaja()
