import os

def controlAcceso():
    os.system("cls")
    clave_correcta = "tienda123"
    intentos = 0

    clave = input("Ingrese la clave: ")
    intentos = intentos + 1

    while clave != clave_correcta:
        print("Clave incorrecta")
        clave = input("Ingrese la clave: ")
        intentos = intentos + 1

    print(f"Acceso permitido en {intentos} intentos")

if __name__ == "__main__":
    controlAcceso()
