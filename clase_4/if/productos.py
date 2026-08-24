import os
os.system("cls")

sacos = 46
peso_sacos = input("Ingrese el peso de los sacos: ")

if peso_sacos < sacos:
    print(f"El peso del saco es {peso_sacos} y es menor que {sacos}, debe revisarse")
else:
    print(f"El peso del saco es {peso_sacos} y cumple con el peso indicado")