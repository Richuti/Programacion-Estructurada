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

    def print(self):
        if self.head == None:
            print("La lista esta vacia")
        else:
            temp = self.head
            while temp != None:
                temp.print()
                temp = temp.next

    def clear(self) -> list[Producto]:
        lista = []
        temp = self.head
        while temp != None:
            prod = Producto(temp.cod, temp.nombre, temp.precio, temp.stock)
            lista.append(prod)
            temp = temp.next
        self.head = None
        return lista

    def remove(self, cod: int):
        if self.head == None:
            return False
        else:
            if self.head.cod == cod:
                temp = self.head
                self.head = self.head.next
                temp.next = None
                return True
            temp = self.head
            while temp.next != None:
                if temp.next.cod == cod:
                    borrar = temp.next
                    temp.next = borrar.next
                    borrar.next = None
                    return True
                elif temp.next.cod > cod:
                    return False
                temp = temp.next
            return False
