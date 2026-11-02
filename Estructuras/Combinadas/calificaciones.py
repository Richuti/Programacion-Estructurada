notas = {
    "Ana": [18, 15, 17, 20],
    "Luis": [12, 14, 10, 16],
    "Maria": [19, 18, 20, 17],
    "Pedro": [10, 11, 13, 12]
}
for estudiante, lista_notas in notas.items():
    promedio = sum(lista_notas) / len(lista_notas)
    print(estudiante + ":", lista_notas, "- Promedio:", promedio)
