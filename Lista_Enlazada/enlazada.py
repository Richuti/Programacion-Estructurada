class Producto:
    def __init__(self, cod: int, nombre: str, precio: float, stock: int):
        self.cod = cod
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.next = None

    def print(self):
        print(f"[{self.cod}]|[{self.nombre}|{self.precio}|{self.stock}]")

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new: Producto):
        if self.head == None:
            self.head = new
            return True
        else:
            if new.cod < self.head.cod:
                new.next = self.head
                self.head = new
                return True
            if new.cod > self.head.cod:
                temp = self.head
                while temp.next != None:
                    if new.cod > temp.next.cod:
                        temp = temp.next
                    elif new.cod == temp.next.cod:
                        return False
                    else:
                        break
                new.next = temp.next
                temp.next = new
                return True
            else:
                return False

lista = LinkedList()
lista.insert(Producto(20, "Arroz", 2.5, 10))
lista.insert(Producto(5, "Leche", 1.8, 30))
lista.insert(Producto(12, "Pan", 0.9, 50))