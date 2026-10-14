import os

estudiante = {
    "carnet": "",
    "nombre": "",
    "parcial1": 0.0,
    "parcial2": 0.0,
    "proyecto": 0.0,
}

estudiantes = []


def agregar_estudiante(estudiantes, carnet, nombre, parcial1, parcial2, proyecto):
    if buscar_estudiante(estudiantes, carnet) != None:
        return False
    if float(parcial1) < 0 or float(parcial1) > 100:
        return False
    if float(parcial2) < 0 or float(parcial2) > 100:
        return False
    if float(proyecto) < 0 or float(proyecto) > 100:
        return False
    estudiante = {
        "carnet": carnet,
        "nombre": nombre,
        "parcial1": float(parcial1),
        "parcial2": float(parcial2),
        "proyecto": float(proyecto),
    }
    estudiantes.append(estudiante.copy())
    return True


def buscar_estudiante(estudiantes, carnet):
    encontrado = None
    for est in range(0, len(estudiantes)):
        if estudiantes[est]["carnet"] == carnet:
            encontrado = est
            break
    return encontrado


def actualizar_calificacion(estudiantes, carnet, campo, nota):
    index = buscar_estudiante(estudiantes, carnet)
    if index == None:
        return False
    if campo != "parcial1" and campo != "parcial2" and campo != "proyecto":
        return False
    nota = float(nota)
    if nota < 0 or nota > 100:
        return False
    estudiantes[index][campo] = nota
    return True


def eliminar_estudiante(estudiantes, carnet):
    index = buscar_estudiante(estudiantes, carnet)
    if index != None:
        estudiantes.pop(index)
        return True
    return False


def guardar_estudiantes(ruta, estudiantes):
    fichero = open(ruta, "w", encoding="utf-8")
    for est in estudiantes:
        fichero.write(est["carnet"] + "\n")
        fichero.write(est["nombre"] + "\n")
        fichero.write(str(est["parcial1"]) + "\n")
        fichero.write(str(est["parcial2"]) + "\n")
        fichero.write(str(est["proyecto"]) + "\n")
    fichero.close()


def cargar_estudiantes(ruta):
    lista = []
    if not os.path.exists(ruta):
        return lista
    fichero = open(ruta, "r", encoding="utf-8")
    carnet = fichero.readline()
    while carnet != "":
        if carnet.strip() != "":
            est = {}
            est["carnet"] = carnet.rstrip("\n")
            est["nombre"] = fichero.readline().rstrip("\n")
            est["parcial1"] = float(fichero.readline().rstrip("\n"))
            est["parcial2"] = float(fichero.readline().rstrip("\n"))
            est["proyecto"] = float(fichero.readline().rstrip("\n"))
            lista.append(est.copy())
        carnet = fichero.readline()
    fichero.close()
    return lista