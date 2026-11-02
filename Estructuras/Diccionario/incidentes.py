ventas = {
    "Ana": 1500,
    "Luis": 2300,
    "Maria": 1800,
    "Pedro": 2100
}
mejor_tecnico = ""
mayor_venta = 0
for tecnico, total in ventas.items():
    print(tecnico + ":", total)
    if total > mayor_venta:
        mayor_venta = total
        mejor_tecnico = tecnico
print("Mayor venta:", mejor_tecnico, "con", mayor_venta)
