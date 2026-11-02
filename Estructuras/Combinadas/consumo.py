ventas = {
    "lunes": [120, 80, 45, 200],
    "martes": [300, 150],
    "miercoles": [90, 60, 110, 40, 75],
    "jueves": [250, 180, 95],
    "viernes": [400, 220, 130, 60]
}
for dia, lista_ventas in ventas.items():
    total = sum(lista_ventas)
    print(dia + ":", lista_ventas, "- Total:", total)
