nombre = []
notas = []

for x in range(3):
    nom = input("Ingrese el nombre del alumno: ")
    nombre.append(nom)
    no1 = int(input("Ingrese la nota 1: "))
    no2 = int(input("Ingrese la nota 2: "))
    notas.append([no1, no2])

for x in range(3):
    print("*" * 10)
    print(f"Nombre: {nombre[x]}")
    print(f"Nota 1: {notas[x][0]}")
    print(f"Nota 2: {notas[x][1]}")
    print("*" * 10)
