class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedListWithSentinels:
    def __init__(self):
        # Create the permanent guards
        self.header = Node()
        self.trailer = Node()
        
        # Make them hold hands initially
        self.header.next = self.trailer
        self.trailer.prev = self.header

    def insert_at_front(self, data):
        new_node = Node(data)
        
        # We are inserting between 'header' and 'header.next'
        # No 'if' checks needed! The steps are always identical:
        
        new_node.next = self.header.next
        new_node.prev = self.header
        
        self.header.next.prev = new_node
        self.header.next = new_node