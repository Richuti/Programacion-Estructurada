import os

def creditoPulperia():
    os.system("cls")
    registrado = input("El cliente esta registrado? (si/no): ")

    if registrado == "si":
        saldo = float(input("Ingrese el saldo pendiente del cliente: "))
        if saldo < 500:
            print("El credito fue autorizado")
        else:
            print("El credito fue rechazado por saldo alto")
    else:
        print("El cliente no esta registrado, no se puede dar credito")

if __name__ == "__main__":
    creditoPulperia()
