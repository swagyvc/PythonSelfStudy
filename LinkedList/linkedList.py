class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head

        self.head = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.insert_at_beginning(30)
ll.insert_at_beginning(20)
ll.insert_at_beginning(10)

ll.print_list()  # Output: 10 -> 20 -> 30 -> None
