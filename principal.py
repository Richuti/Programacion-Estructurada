from nomina import *

def main():
    registros = cargar_nomina()
    print(f"Se han cargado {registros} registros")

    agregar_empleado()
    agregar_empleado()

    guardar_nomina()

main()
