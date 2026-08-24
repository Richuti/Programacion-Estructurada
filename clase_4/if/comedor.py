import os
os.system("cls")

sin_recargo = 300
recargo = float(input("Ingrese el total de recargo: "))

if recargo < sin_recargo:
    total = recargo + 40
    print(f"La entrega le saldria por {total}")
else:
    print("La entrega es gratuita")