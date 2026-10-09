from nomina import *
import os

def main():
    registros = cargar_nomina()
    opcion = 0
    while True:
        os.system("cls")
        print("--------------------------------")
        print("----- GESTION DE NOMINA -----")
        print("--------------------------------")
        print("1. Agregar Empleado")
        print("2. Buscar Empleado")
        print("3. Eliminar Empleado")
        print("4. Actualizar Empleado")
        print("5. Guardar Nomina")
        print("6. Cargar Nomina")
        print("7. Salir")
        opcion = int(input("Ingrese una opcion: "))
        match opcion:
            case 1:
                agregar_empleado()
            case 2:
                buscar_empleado()
            case 3:
                eliminar_empleado()
            case 4:
                actualizar_empleado()
            case 5:
                guardar_nomina()
            case 6:
                cargar_nomina()
            case 7:
                break
            case _:
                print("Opcion no valida")

main()  