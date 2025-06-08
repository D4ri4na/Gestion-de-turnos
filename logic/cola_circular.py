from node import Node

class ColaCircular:
    def __init__(self):
        self.head = None
        self.general_counter = 0

    def esta_vacia(self):
        return self.head is None

    def encolar(self, value):
        new_node = Node(value)
        if self.esta_vacia():
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def encolar_al_principio(self, value):
        new_node = Node(value)
        if self.esta_vacia():
            self.head = new_node
            self.head.next = self.head
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node

    def encolar_al_final(self, value):
        new_node = Node(value)
        if self.esta_vacia():
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def desencolar(self):
        if self.esta_vacia():
            return None
        temp = self.head
        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
        return temp

    def remove_ticket(self, ticket_to_remove):
        if self.esta_vacia():
            return False
        current = self.head
        previous = None
        while True:
            if current.value == ticket_to_remove:
                if previous is not None:
                    previous.next = current.next
                    if current == self.head:
                        self.head = current.next
                else:
                    if self.head.next == self.head:
                        self.head = None
                    else:
                        last = self.head
                        while last.next != self.head:
                            last = last.next
                        last.next = self.head.next
                        self.head = self.head.next
                return True
            previous = current
            current = current.next
            if current == self.head:
                break
        return False

    def mostrar(self):
        if self.esta_vacia():
            return []
        items = []
        current = self.head
        while True:
            items.append(current.value)
            current = current.next
            if current == self.head:
                break
        return items

