import os

def productos_a_reponer(existencias, limite):
    faltantes = []

    for producto in existencias:
        if existencias[producto] < limite:
            faltantes.append(producto)

    return faltantes


def probar_inventario():
    os.system("cls")
    print("RETO 5: Inventario minimo")
    print("Recibe las existencias y un limite, y devuelve los productos a reponer.")
    print()

    bodega = {"Arroz": 20, "Frijoles": 5, "Aceite": 12, "Azucar": 3}

    print("Prueba 1 -> limite 10:", productos_a_reponer(bodega, 10))
    print("Prueba 2 -> limite 25:", productos_a_reponer(bodega, 25))
    print("Prueba 3 -> limite 1:", productos_a_reponer(bodega, 1))

if __name__ == "__main__":
    probar_inventario()
