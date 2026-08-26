import os
os.system("cls")

combustible = 10.0

while combustible > 2:
    gasto = float(input("Ingrese el combustible gastado en el recorrido: "))
    combustible = combustible - gasto
    print(f"Combustible disponible: {combustible} litros")

print("Alerta: el combustible llego al nivel minimo")
