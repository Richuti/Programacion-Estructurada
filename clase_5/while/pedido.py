import os
os.system("cls")

precio = 25

unidades = int(input("Ingrese las unidades del pedido (1 a 100): "))

while unidades < 1 or unidades > 100:
    print("La cantidad no es valida")
    unidades = int(input("Ingrese las unidades del pedido (1 a 100): "))

total = unidades * precio

print(f"Pedido confirmado de {unidades} unidades")
print(f"El monto final es {total}")
