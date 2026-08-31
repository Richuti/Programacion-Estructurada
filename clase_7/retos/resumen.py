import os

def resumen_semanal(ventas):
    total = sum(ventas)
    promedio = total / len(ventas)
    minima = min(ventas)
    maxima = max(ventas)
    return total, promedio, minima, maxima


def probar_resumen():
    os.system("cls")
    print("RETO 4: Resumen semanal")
    print("Recibe una lista de ventas y devuelve total, promedio, minima y maxima.")
    print()

    print("Prueba 1 ->", resumen_semanal([100, 200, 300, 400, 500]))
    print("Prueba 2 ->", resumen_semanal([50, 50, 50]))
    print("Prueba 3 ->", resumen_semanal([1200.5, 800, 950.75]))

if __name__ == "__main__":
    probar_resumen()
