accesos = ["laptop", "celular", "tablet", "laptop", "celular", "laptop", "impresora", "celular", "laptop"]
conteo = {}
for dispositivo in accesos:
    if dispositivo not in conteo:
        conteo[dispositivo] = 0
    conteo[dispositivo] += 1
print(conteo)
for dispositivo, cantidad in conteo.items():
    print(dispositivo + ":", cantidad)
