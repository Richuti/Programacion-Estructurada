import os
os.system("cls")

suma = 0
satisfechos = 0

for cliente in range(1, 11):
    nota = int(input(f"Ingrese la valoracion del cliente {cliente} (1 a 5): "))
    suma = suma + nota
    if nota >= 4:
        satisfechos = satisfechos + 1

promedio = suma / 10

print(f"El promedio de valoraciones es {promedio}")
print(f"{satisfechos} clientes calificaron con 4 o 5")
