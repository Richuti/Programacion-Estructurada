import os

def calcular_nota_final(nota1, nota2, nota3, peso1, peso2, peso3):
    final = (nota1 * peso1 / 100) + (nota2 * peso2 / 100) + (nota3 * peso3 / 100)

    if final >= 90:
        clasificacion = "Excelente"
    elif final >= 80:
        clasificacion = "Muy bueno"
    elif final >= 60:
        clasificacion = "Aprobado"
    else:
        clasificacion = "Reprobado"

    return final, clasificacion


def probar_nota():
    os.system("cls")
    print("RETO 7: Nota final")
    print("Recibe tres notas y sus ponderaciones, devuelve nota final y clasificacion.")
    print()

    print("Prueba 1 -> 90, 85, 95 con 30/30/40:", calcular_nota_final(90, 85, 95, 30, 30, 40))
    print("Prueba 2 -> 60, 55, 70 con 25/25/50:", calcular_nota_final(60, 55, 70, 25, 25, 50))
    print("Prueba 3 -> 40, 50, 45 con 30/30/40:", calcular_nota_final(40, 50, 45, 30, 30, 40))

if __name__ == "__main__":
    probar_nota()
