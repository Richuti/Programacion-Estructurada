import os

def entregaComedor():
    os.system("cls")
    sin_recargo = 300
    recargo = float(input("Ingrese el total de recargo: "))

    if recargo < sin_recargo:
        total = recargo + 40
        print(f"La entrega le saldria por {total}")
    else:
        print("La entrega es gratuita")

if __name__ == "__main__":
    entregaComedor()
