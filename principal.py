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
                id = input("Ingrese el ID del empleado a buscar: ")
                index = buscar_empleado(id)
                if index != None:
                    print(f"Empleado encontrado: {nomina[index]['nombre']}")
                    print(f"Salario: {nomina[index]['salario']}")
                    print(f"Antiguedad: {nomina[index]['antiguedad']}")
                    print(f"Departamento: {nomina[index]['departamento']}")
                else:
                    print("Empleado no encontrado")
            case 3:
                id = input("Ingrese el ID del empleado a eliminar: ")
                if eliminar_empleado(id):
                    print("Empleado eliminado")
                else:
                    print("Empleado no encontrado")
            case 4:
                id = input("Ingrese el ID del empleado a actualizar: ")
                if actualizar_empleado(id):
                    print("Empleado actualizado")
                else:
                    print("Empleado no encontrado")
            case 5:
                guardar_nomina()
            case 6:
                cargar_nomina()
            case 7:
                break
            case _:
                print("Opcion no valida")
        input("Presione Enter para continuar...")

main()  