import os

def descuentoProporcional():
    os.system("cls")

    try:
        monto = float(input("Ingrese el monto: "))
        base = float(input("Ingrese la base: "))

        porcentaje = (monto / base) * 100

        print(f"El porcentaje es: {porcentaje}")
    except ValueError:
        print("Error: el monto y la base deben ser valores numericos")
    except ZeroDivisionError:
        print("Error: la base no puede ser cero")

if __name__ == "__main__":
    descuentoProporcional()
