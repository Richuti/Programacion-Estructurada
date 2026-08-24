import os
os.system("cls")

total_producido = 0
total_vendido = 0

for dia in range(1, 7):
    producido = int(input(f"Ingrese el pan producido el dia {dia}: "))
    vendido = int(input(f"Ingrese el pan vendido el dia {dia}: "))
    total_producido = total_producido + producido
    total_vendido = total_vendido + vendido

sobrante = total_producido - total_vendido

print(f"El total producido es {total_producido}")
print(f"El total vendido es {total_vendido}")
print(f"El sobrante de la semana es {sobrante}")
