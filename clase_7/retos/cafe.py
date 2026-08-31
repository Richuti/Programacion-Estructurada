import os

def clasificar_cafe(humedad):
    if humedad >= 10 and humedad <= 12:
        return "aceptado"
    else:
        return "revisar"


def probar_cafe():
    os.system("cls")
    print("RETO 2: Clasificacion de cafe")
    print("Devuelve 'aceptado' si la humedad esta entre 10 y 12.")
    print()

    print("Prueba 1 -> humedad 11:", clasificar_cafe(11))
    print("Prueba 2 -> humedad 9.5:", clasificar_cafe(9.5))
    print("Prueba 3 -> humedad 12:", clasificar_cafe(12))
    print("Prueba 4 -> humedad 15:", clasificar_cafe(15))

if __name__ == "__main__":
    probar_cafe()
