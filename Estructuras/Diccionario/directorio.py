contactos = {
    "Ana": "0414-1234567",
    "Luis": "0424-7654321",
    "Maria": "0412-5558899",
    "Pedro": "0416-3332211"
}
nombre = input("Ingrese el nombre del contacto: ")
if nombre in contactos:
    print("Telefono de", nombre + ":", contactos[nombre])
else:
    print("El contacto", nombre, "no existe")
