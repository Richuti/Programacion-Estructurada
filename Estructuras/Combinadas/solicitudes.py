pedidos = [
    {"cliente": "Ana", "productos": ["laptop", "mouse", "teclado"]},
    {"cliente": "Luis", "productos": ["monitor"]},
    {"cliente": "Maria", "productos": ["celular", "cargador", "audifonos", "forro"]},
    {"cliente": "Pedro", "productos": ["impresora", "cartucho"]}
]
for pedido in pedidos:
    cantidad = len(pedido["productos"])
    print("Cliente:", pedido["cliente"], "- Productos:", pedido["productos"], "- Cantidad:", cantidad)
