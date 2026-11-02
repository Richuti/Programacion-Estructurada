latencias = []
for i in range(10):
    latencia = float(input(f"Ingrese la latencia {i + 1} (ms): "))
    latencias.append(latencia)
latencias.sort()
print("De menor a mayor:", latencias)
latencias.sort(reverse=True)
print("De mayor a menor:", latencias)
