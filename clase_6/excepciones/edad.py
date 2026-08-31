import os

def edadRegistro():
    os.system("cls")

    try:
        edad = int(input("Ingrese su edad: "))
    except ValueError:
        print("Error: la edad debe ser un numero entero")
    else:
        if edad < 0 or edad > 120:
            print("Error: la edad esta fuera del rango permitido")
        else:
            print(f"Registro aceptado, su edad es: {edad}")

if __name__ == "__main__":
    edadRegistro()
