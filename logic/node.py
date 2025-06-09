class NodeHash:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    