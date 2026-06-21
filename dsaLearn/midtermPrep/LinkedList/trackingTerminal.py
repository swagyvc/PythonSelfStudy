class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class SentinelDoublyLinkedList:
    def __init__(self):
        # Create the dummy boundary nodes
        self.header = Node()
        self.trailer = Node()
        
        # Link them to each other initially
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def insert_between(self, data, predecessor, successor):
        """Adds data between two existing nodes."""
        new_node = Node(data)
        new_node.prev = predecessor
        new_node.next = successor
        
        predecessor.next = new_node
        successor.prev = new_node
        
        self.size += 1
        return new_node

    def remove_node(self, node):
        """Removes a node from the list by unlinking it."""
        predecessor = node.prev
        successor = node.next
        
        predecessor.next = successor
        successor.prev = predecessor
        
        self.size -= 1
        return node.data

    def add_to_front(self, data):
        """Inserts right after the header sentinel."""
        return self.insert_between(data, self.header, self.header.next)

    def add_to_back(self, data):
        """Inserts right before the trailer sentinel."""
        return self.insert_between(data, self.trailer.prev, self.trailer)

    def remove_from_front(self):
        """Removes the first real data item."""
        if self.size == 0:
            print("List is empty.")
            return None
        return self.remove_node(self.header.next)

    def display(self):
        """Traverses from the first real node to the last."""
        current = self.header.next
        items = []
        while current != self.trailer:
            items.append(str(current.data))
            current = current.next
        print("[Header] <-> " + " <-> ".join(items) + " <-> [Trailer]")


# --- Test Execution ---
if __name__ == "__main__":
    cache_log = SentinelDoublyLinkedList()

    print("Adding items to back:")
    cache_log.add_to_back("Page_A")
    cache_log.add_to_back("Page_B")
    cache_log.add_to_back("Page_C")
    cache_log.display()

    print("\nAdding item to front:")
    cache_log.add_to_front("New_Page_Zero")
    cache_log.display()

    print("\nRemoving from front:")
    cache_log.remove_from_front()
    cache_log.display()