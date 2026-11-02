nombres = ["laptop", "mouse", "teclado", "monitor"]
precios = [850, 15, 30, 220]
existencias = [10, 0, 25, 4]
for nombre, precio, existencia in zip(nombres, precios, existencias):
    print("Producto:", nombre, "- Precio:", precio, "- Existencia:", existencia)
