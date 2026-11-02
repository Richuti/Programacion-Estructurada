registro = "host=localhost;puerto=1433;bd=ventas"
configuracion = {}
for dato in registro.split(";"):
    clave, valor = dato.split("=")
    configuracion[clave] = valor
print(registro)
print(configuracion)
print("Host:", configuracion["host"])
print("Puerto:", configuracion["puerto"])
print("Base de datos:", configuracion["bd"])
