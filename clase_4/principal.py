import os
def main():
    os.system("cls") #Limpiar la terminal
    nombre_asignatura = input("Ingrese la asignatura: ") #La variable nombre_asignatura es de tipo str
    respuesta = input("La asignatura está activa? (True/False o 1/0): ").strip().lower()
    is_active = respuesta in ("true", "1", "si", "sí") #La variable is_active es de tipo bool
    numero_de_creditos = int(input("Ingrese el número de créditos: ")) #La variable numero_de_creditos es de tipo int
    nota = float(input("Ingrese la nota: ")) #La variable nota es de tipo float

    os.system("cls") #Limpiar la terminal
    print(f"La asignatura {nombre_asignatura} tiene {numero_de_creditos} créditos y la nota es {nota}")
    print(f"La asignatura {nombre_asignatura} está activa: {is_active}")

main()