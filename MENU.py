import os
from examen import *

def main():
    registros = cargar_estudiantes("estudiantes.txt")
    opcion = 0
    while True:
        os.system("cls")
        print("--------------------------------")
        print("----- GESTION DE ESTUDIANTES -----")
        print("--------------------------------")
        print("1. Agregar Estudiante")
        print("2. Buscar Estudiante")
        print("3. Actualizar Estudiante")
        print("4. Eliminar Estudiante")
        print("5. Guardar Estudiantes")
        print("6. Cargar Estudiantes")
        print("7. Salir")
        opcion = int(input("Ingrese una opcion: "))
        match opcion:
            case 1:
                carnet = input("Ingrese el carnet del estudiante: ")
                nombre = input("Ingrese el nombre del estudiante: ")
                parcial1 = float(input("Ingrese la nota del parcial 1: "))
                parcial2 = float(input("Ingrese la nota del parcial 2: "))
                proyecto = float(input("Ingrese la nota del proyecto: "))
                if agregar_estudiante(registros, carnet, nombre, parcial1, parcial2, proyecto):
                    guardar_estudiantes("estudiantes.txt", registros)
            case 2:
                carnet = input("Ingrese el carnet del estudiante a buscar: ")
                index = buscar_estudiante(registros, carnet)
                if index != None:
                    print(f"Estudiante encontrado: {registros[index]['nombre']}")   
                else:
                    print("Estudiante no encontrado")
            case 3:
                carnet = input("Ingrese el carnet del estudiante a actualizar: ")
                print("1. Parcial 1")
                print("2. Parcial 2")
                print("3. Proyecto")
                opcion_campo = int(input("Ingrese el campo a actualizar: "))
                match opcion_campo:
                    case 1:
                        campo = "parcial1"
                    case 2:
                        campo = "parcial2"
                    case 3:
                        campo = "proyecto"
                    case _:
                        campo = ""
                if campo == "":
                    print("Opcion invalida")
                else:
                    nota = float(input("Ingrese la nueva nota: "))
                    actualizar_calificacion(registros, carnet, campo, nota)
            case 4:
                carnet = input("Ingrese el carnet del estudiante a eliminar: ")
                eliminar_estudiante(registros, carnet)
            case 5:
                guardar_estudiantes("estudiantes.txt", registros)   
            case 6:
                registros = cargar_estudiantes("estudiantes.txt")
            case 7:
                break
        input("Presione Enter para continuar...")

main()