import os

def calificacionEstudiante():
    os.system("cls")

    try:
        calificacion = float(input("Ingrese la calificacion: "))
    except ValueError:
        print("Error: la calificacion debe ser un valor numerico")
    else:
        if calificacion >= 0 and calificacion <= 100:
            print(f"La calificacion {calificacion} esta entre 0 y 100")
        else:
            print(f"La calificacion {calificacion} esta fuera del rango de 0 a 100")

if __name__ == "__main__":
    calificacionEstudiante()
