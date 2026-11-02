existencias = [5, 0, 12, 0, 8, 3, 0, 20]
posiciones_agotadas = []
for posicion, existencia in enumerate(existencias):
    if existencia == 0:
        posiciones_agotadas.append(posicion)
print(existencias)
print(posiciones_agotadas)
print(len(posiciones_agotadas))
