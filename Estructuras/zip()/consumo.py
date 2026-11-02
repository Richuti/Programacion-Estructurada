dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]
semana_1 = [450, 300, 520, 610, 700]
semana_2 = [500, 280, 520, 650, 640]
for dia, venta_1, venta_2 in zip(dias, semana_1, semana_2):
    diferencia = venta_2 - venta_1
    print(dia + ": semana 1 =", venta_1, "| semana 2 =", venta_2, "| diferencia =", diferencia)
