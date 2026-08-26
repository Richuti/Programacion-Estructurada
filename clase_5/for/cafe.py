import os

def pesoCafe():
    os.system("cls")
    peso_total = 0

    for saco in range(1, 6):
        peso = float(input(f"Ingrese el peso del saco {saco}: "))
        peso_total = peso_total + peso

    print(f"El peso total recibido es {peso_total} libras")

if __name__ == "__main__":
    pesoCafe()
