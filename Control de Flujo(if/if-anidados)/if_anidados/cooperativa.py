import os

def calidadCooperativa():
    os.system("cls")
    humedad = float(input("Ingrese la humedad del cafe en porcentaje: "))

    if humedad <= 12:
        defectos = int(input("Ingrese la cantidad de defectos del lote: "))
        if defectos <= 5:
            print("El lote es de primera calidad")
        else:
            print("El lote es de segunda calidad")
    else:
        print("El lote es rechazado por exceso de humedad")

if __name__ == "__main__":
    calidadCooperativa()
