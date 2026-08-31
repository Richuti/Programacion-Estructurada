import os

def conversionMoneda():
    os.system("cls")

    try:
        monto = float(input("Ingrese el monto en cordobas: "))
        tasa = float(input("Ingrese la tasa de cambio: "))

        equivalente = monto / tasa

        print(f"El equivalente en dolares es: {round(equivalente, 2)}")
    except ValueError:
        print("Error: el monto y la tasa deben ser valores numericos")
    except ZeroDivisionError:
        print("Error: la tasa de cambio no puede ser cero")

if __name__ == "__main__":
    conversionMoneda()
