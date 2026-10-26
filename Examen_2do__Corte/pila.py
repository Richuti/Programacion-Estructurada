class Product:
    def __init__(self, id:int, nombre:str, precio:float, stock:int):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.next = None

    def print(self):
        print(f"[ID: {self.id} | Nombre: {self.nombre} | Precio: {self.precio} | Stock: {self.stock}]")

class Stack:
    def __init__(self):
        self.top = None

    def push(self, new: Product):
        if self.top == None:
            self.top = new
        else:
            new.next = self.top
            self.top = new

    def pop(self) -> Product:
        prod = None
        if not self.isEmpty():
            prod = self.top
            self.top = self.top.next
            prod.next = None
        return prod

    def peek(self) -> Product:
        return self.top

    def isEmpty(self) -> bool:
        if self.top == None:
            return True
        else:
            return False

    def search(self, id:int) -> Product:
        temp = self.top
        while temp != None:
            if temp.id == id:
                return temp
            temp = temp.next
        return None

    def print(self):
        temp = self.top
        while temp != None:
            temp.print()
            temp = temp.next

    def clear(self) -> list[Product]:
        lista: list[Product] = []
        while not self.isEmpty():
            prod: Product = self.pop()
            lista.append(prod)
        return lista
