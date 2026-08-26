import os

def promocionTienda():
    os.system("cls")
    monto_compra = float(input("Ingrese el total de la compra: "))

    if monto_compra > 1500:
        total_compra = monto_compra - (monto_compra * 0.10)
        print(f"El total de la compra es: {total_compra}")
    else:
        print(f"El total de la compra es: {monto_compra}")

if __name__ == "__main__":
    promocionTienda()
