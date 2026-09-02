import os

def importacionControlada():
    os.system("cls")

    try:
        import modulo_inexistente
        print("El modulo se importo correctamente")
    except ModuleNotFoundError:
        print("Error: no se encontro el modulo 'modulo_inexistente'")
        print("Debe revisar que el nombre este bien escrito,")
        print("que el archivo exista en la carpeta del proyecto")
        print("o que la libreria este instalada con pip.")

if __name__ == "__main__":
    importacionControlada()
