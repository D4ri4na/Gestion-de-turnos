from node import Node

class Queue:
    def __init__(self):
        self.head = None

    def enqueue(self, priority, value): ##encolar
        new_node = Node(priority, value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def dequeue(self): ##desencolar
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp