import os

def leer_monto():
    return input("Ingrese el monto en cordobas: ")


def validar_monto(texto):
    try:
        monto = float(texto)
    except ValueError:
        return None
    else:
        if monto < 0:
            return None
        return monto


def convertir_a_dolares(monto, tasa):
    return monto / tasa


def presentar_resultado(monto, dolares):
    print(f"C$ {monto} equivalen a $ {round(dolares, 2)}")


def probar_moneda():
    os.system("cls")
    print("RETO 6: Conversion de moneda")
    print("Separada en leer, validar, convertir y presentar.")
    print()

    print("Prueba 1 -> validar '1000':", validar_monto("1000"))
    print("Prueba 2 -> validar 'mil':", validar_monto("mil"))
    print("Prueba 3 -> validar '-50':", validar_monto("-50"))
    print("Prueba 4 -> convertir 1000 a tasa 36.80:", round(convertir_a_dolares(1000, 36.80), 2))
    print()

    texto = leer_monto()
    monto = validar_monto(texto)

    if monto is None:
        print("Error: el monto no es valido")
    else:
        presentar_resultado(monto, convertir_a_dolares(monto, 36.80))

if __name__ == "__main__":
    probar_moneda()
