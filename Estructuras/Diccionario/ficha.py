producto = {
    "modelo": "Router AX3000",
    "ip": "192.168.1.1",
    "estado": "activo",
    "sistema_operativo": "OpenWrt",
    "existencia": 15
}
print(producto)
print("Modelo:", producto["modelo"])
print("IP:", producto["ip"])
print("Existencia actual:", producto["existencia"])
producto["existencia"] = 10
print("Existencia modificada:", producto["existencia"])
print(producto)
