evento_1 = ["Ana", "Luis", "Maria", "Pedro", "Carla"]
evento_2 = ["Luis", "Carla", "Jose", "Sofia", "Ana"]
asistentes_1 = set(evento_1)
asistentes_2 = set(evento_2)
ambos = asistentes_1 & asistentes_2
solo_primero = asistentes_1 - asistentes_2
print("Asistieron a ambos eventos:", ambos)
print("Asistieron solo al primero:", solo_primero)
