from node import NodeHash

class HashMap:
    def __init__(self):
        self.CAPACITY = 3
        self.DEFAULT_LOAD_FACTOR = 0.75
        self.table = [None] * self.CAPACITY
        self.size = 0
    
    def _hash(self, key):
        if key == 'G':
            return 0
        elif key == 'P':
            return 1
        elif key == 'C':
            return 2
        return 0
    
    def put(self, key, value):
        if self.size >= self.CAPACITY * self.DEFAULT_LOAD_FACTOR:
            self._resize()

        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = NodeHash(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current.next is not None:
                current = current.next
            current.next = NodeHash(key, value)
            self.size += 1

    def get_tickets_type(self, key):
        index = self._hash(key)
        tickets = []
        current = self.table[index]

        while current:
            if current.key == key:
                tickets.append(current.value)
            current = current.next

        return tickets
    
    def remove_ticket(self, ticket_id):
        key = ticket_id[0]
        index = self._hash(key)
        current = self.table[index]

        if current is None:
            return False
        
        if current.key == key and current.value == ticket_id:
            self.table[index] = current.next
            self.size -= 1
            return True
        
        while current.next:
            if current.next.key == key and current.next.value == ticket_id:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next

        return False
    
    def exists_ticket(self, ticket_id):
        key = ticket_id[0]
        index = self._hash(key)
        current = self.table[index]

        while current:
            if current.key == key and current.value == ticket_id:
                return True
            current = current.next
        return False
    
    def _resize(self):
        old_table = self.table
        self.CAPACITY *= 2
        self.table = [None] * self.CAPACITY
        self.size = 0

        for node in old_table:
            while node is not None:
                self.put(node.key, node.value)
                node = node.next

