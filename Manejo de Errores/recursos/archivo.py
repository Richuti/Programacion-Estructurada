import os

def archivoReportes():
    os.system("cls")

    try:
        archivo = open("reportes.txt", "r")
        contenido = archivo.read()
        archivo.close()
        print("Contenido del reporte:")
        print(contenido)
    except FileNotFoundError:
        print("Error: el archivo reportes.txt no existe")
    finally:
        print("La operacion de lectura termino")

if __name__ == "__main__":
    archivoReportes()
