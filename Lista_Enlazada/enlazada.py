class Producto:
    def __init__(self, cod: int, nombre: str, precio: float, stock: int):
        self.cod = cod
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def print(self):
        print(f"[{self.cod}]|[{self.nombre}|{self.precio}|{self.stock}]")

class LinkedList:
    def __init__(self):
        head=None

    def insert(self, new: Producto):
        if self.head == None:
            self.head = new
        else: 
            if new.cod < self.head.cod:
                new.next = self.head
                self.head=new
            if new.cod > self.head.cod:
                temp = self.head
                temp = temp.next
                while temp.next != None:
                    if new.cod > temp.cod:
                        temp = temp.next
                    else:
                        new.next = temp
                        temp = new
                        break
            
