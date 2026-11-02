inventario = {
    "laptop": 10,
    "mouse": 25,
    "teclado": 15,
    "monitor": 8
}
movimientos = [
    ("laptop", "salida", 3),
    ("mouse", "entrada", 10),
    ("monitor", "salida", 2),
    ("teclado", "salida", 20),
    ("laptop", "entrada", 5)
]
print("Inventario inicial:", inventario)
for producto, tipo, cantidad in movimientos:
    if tipo == "entrada":
        inventario[producto] += cantidad
        print("Entrada de", cantidad, producto)
    elif inventario[producto] >= cantidad:
        inventario[producto] -= cantidad
        print("Salida de", cantidad, producto)
    else:
        print("No hay suficiente", producto, "para sacar", cantidad)
print("Inventario final:", inventario)
