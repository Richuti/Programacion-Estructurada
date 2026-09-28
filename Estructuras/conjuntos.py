import os

def asistenciaClases():
    os.system("cls")

    # Los conjuntos no permiten elementos repetidos
    lunes = set()
    miercoles = set()

    for x in range(3):
        alumno = input(f"Alumno {x + 1} que asistio el lunes: ")
        lunes.add(alumno)

    for x in range(3):
        alumno = input(f"Alumno {x + 1} que asistio el miercoles: ")
        miercoles.add(alumno)

    print("*" * 30)
    print("   REPORTE DE ASISTENCIA")
    print("*" * 30)
    print(f"Asistieron el lunes: {lunes}")
    print(f"Asistieron el miercoles: {miercoles}")
    print(f"Asistieron algun dia: {lunes | miercoles}")
    print(f"Asistieron ambos dias: {lunes & miercoles}")
    print(f"Solo asistieron el lunes: {lunes - miercoles}")
    print(f"Solo asistieron el miercoles: {miercoles - lunes}")
    print(f"Total de alumnos distintos: {len(lunes | miercoles)}")
    print("*" * 30)

if __name__ == "__main__":
    asistenciaClases()
