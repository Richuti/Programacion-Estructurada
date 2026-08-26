import os

def ventasMinisuper():
    os.system("cls")
    total = 0

    for dia in range(1, 8):
        venta = float(input(f"Ingrese la venta del dia {dia}: "))
        total = total + venta

    promedio = total / 7

    print(f"El total de la semana es {total}")
    print(f"El promedio diario es {promedio}")

if __name__ == "__main__":
    ventasMinisuper()
