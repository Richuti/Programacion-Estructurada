import os

def menuOpciones():
    os.system("cls")

    print("1. Consultar saldo")
    print("2. Realizar deposito")
    print("3. Salir")

    try:
        opcion = int(input("Seleccione una opcion: "))
    except ValueError:
        print("Error: la opcion debe ser un numero entero")
    else:
        # El else solo confirma que la conversion funciono,
        # el rango se sigue validando aparte
        if opcion == 1:
            print("Consultando saldo...")
        elif opcion == 2:
            print("Realizando deposito...")
        elif opcion == 3:
            print("Saliendo...")
        else:
            print("Error: esa opcion no esta en el menu")

if __name__ == "__main__":
    menuOpciones()
