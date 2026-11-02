productos = [
    {"nombre": "Laptop Lenovo", "categoria": "computadoras"},
    {"nombre": "Mouse Logitech", "categoria": "accesorios"},
    {"nombre": "Celular Xiaomi", "categoria": "telefonos"},
    {"nombre": "Laptop Dell", "categoria": "computadoras"},
    {"nombre": "Teclado Redragon", "categoria": "accesorios"},
    {"nombre": "Celular Samsung", "categoria": "telefonos"},
    {"nombre": "Monitor LG", "categoria": "pantallas"}
]
categorias = set()
for producto in productos:
    categorias.add(producto["categoria"])
print("Categorias diferentes:", categorias)
print("Total de categorias:", len(categorias))
