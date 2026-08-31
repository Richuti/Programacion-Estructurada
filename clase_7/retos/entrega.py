import os

def calcular_tarifa(distancia, zona):
    tarifa_base = 50

    if zona == "urbana":
        return tarifa_base + (distancia * 10)
    else:
        return tarifa_base + (distancia * 18)


def probar_entrega():
    os.system("cls")
    print("RETO 3: Tarifa de entrega")
    print("Devuelve la tarifa segun la distancia y si la zona es urbana o rural.")
    print()

    print("Prueba 1 -> 5 km urbana:", calcular_tarifa(5, "urbana"))
    print("Prueba 2 -> 5 km rural:", calcular_tarifa(5, "rural"))
    print("Prueba 3 -> 0 km urbana:", calcular_tarifa(0, "urbana"))

if __name__ == "__main__":
    probar_entrega()
