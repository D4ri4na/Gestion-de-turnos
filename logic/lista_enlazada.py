from node import Node

class ListaEnlazada:
    def __init__(self):
        self.head = None

    def agregar(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def eliminar(self, ticket_id):
        if self.head is None:
            return False
        
        if self.head.data[0] == ticket_id:
            self.head = self.head.next
            return True
        
        current = self.head
        while current.next is not None:
            if current.next.data[0] == ticket_id:
                current.next = current.next.next
                return True
            current = current.next

        return False
    
    def mostrar(self):
        tickets = []
        current = self.head
        while current:
            tickets.append(current.data)
            current = current.next
        return tickets
    
    def is_empty(self):
        return self.head is None