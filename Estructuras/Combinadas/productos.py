productos = [
    {"nombre": "Laptop Lenovo", "ram": 16, "precio": 850},
    {"nombre": "Laptop HP", "ram": 8, "precio": 520},
    {"nombre": "Tablet Samsung", "ram": 4, "precio": 300},
    {"nombre": "Laptop Dell", "ram": 32, "precio": 1400},
    {"nombre": "Celular Xiaomi", "ram": 8, "precio": 250}
]
precio_minimo = float(input("Ingrese el precio minimo: "))
for producto in productos:
    if producto["precio"] > precio_minimo:
        print(producto["nombre"], "- RAM:", producto["ram"], "GB - Precio:", producto["precio"])
