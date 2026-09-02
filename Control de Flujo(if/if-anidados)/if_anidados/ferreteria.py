import os

def totalFerreteria():
    os.system("cls")
    tipo = input("Ingrese el tipo de cliente (mayorista/minorista): ")
    compra = float(input("Ingrese el monto de la compra: "))

    if tipo == "mayorista":
        if compra >= 10000:
            total = compra - (compra * 0.15)
        else:
            total = compra - (compra * 0.08)
    else:
        if compra >= 2000:
            total = compra - (compra * 0.05)
        else:
            total = compra

    print(f"El total a pagar es {total}")

if __name__ == "__main__":
    totalFerreteria()
