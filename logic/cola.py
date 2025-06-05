
from node import Node

class ColaPrioridad:
    def __init__(self):
        self.head = None

    def encolar(self, priority, value):
        new_node = Node(priority, value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def desencolar(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp

    def remove_ticket(self, ticket_to_remove):
        current = self.head
        previous = None
        while current is not None:
            if current.value == ticket_to_remove:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next
        return False

    def mostrar(self):
        items = []
        current = self.head
        while current is not None:
            items.append((current.value, current.priority))
            current = current.next
        return items
