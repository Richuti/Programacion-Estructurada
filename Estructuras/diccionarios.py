import os

def notasAlumnos():
    os.system("cls")

    # Diccionario: la clave es el nombre del alumno y el valor su nota
    notas = {}

    for x in range(3):
        nombre = input(f"Ingrese el nombre del alumno {x + 1}: ")
        nota = float(input(f"Ingrese la nota de {nombre}: "))
        notas[nombre] = nota

    print("*" * 30)
    print("   REGISTRO DE NOTAS")
    print("*" * 30)
    for nombre, nota in notas.items():
        if nota >= 60:
            estado = "Aprobado"
        else:
            estado = "Reprobado"
        print(f"{nombre}: {nota} - {estado}")
    print("*" * 30)

    buscar = input("Ingrese el nombre del alumno a buscar: ")
    if buscar in notas:
        print(f"La nota de {buscar} es {notas[buscar]}")
    else:
        print(f"El alumno {buscar} no esta registrado")

    promedio = sum(notas.values()) / len(notas)
    print(f"El promedio del grupo es {promedio:.2f}")

if __name__ == "__main__":
    notasAlumnos()
