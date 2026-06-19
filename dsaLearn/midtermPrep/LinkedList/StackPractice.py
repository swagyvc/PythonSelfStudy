class FriendNode:
    def __init__(self, name):
        self.data = name
        self.next: FriendNode | None = None
        self.prev: FriendNode | None = None

class FriendStack:
    def __init__(self):
        # In a stack, 'head' is the top of the stack
        self.head: FriendNode | None = None

    def push(self, name):
        """Add an item to the top of the stack (Insert Front)"""
        new_friend = FriendNode(name)
        
        # Scenario 1: Stack is empty
        if self.head is None:
            self.head = new_friend
            return
            
        # Scenario 2: Stack has items. Hook up the pointers two-ways.
        new_friend.next = self.head  # New node points forward to old top
        self.head.prev = new_friend  # Old top points backward to new node
        self.head = new_friend       # Move the top marker to the new node

    def pop(self):
        """Remove and return the item from the top of the stack (Delete Front)"""
        # Scenario 1: Stack is empty
        if self.head is None:
            return None
            
        popped_name = self.head.data
        
        # Scenario 2: Only one item left in the stack
        if self.head.next is None:
            self.head = None
            return popped_name
            
        # Scenario 3: Multiple items in the stack
        self.head = self.head.next  # Move top marker down to the next node
        self.head.prev = None       # Disconnect from the old top node
        
        return popped_name

    def display(self):
        """Displays stack from Top to Bottom"""
        current = self.head
        print("--- TOP OF STACK ---")
        while current is not None:
            print(f"|  {current.data}  |")
            current = current.next
        print("--------------------")

stack = FriendStack()

# Push items onto the stack
stack.push("Thai")
stack.push("Hieu")
stack.push("Misa")

stack.display()
# Output order from top to bottom: Misa -> Hieu -> Thai

# Pop the top item off
print(f"\nPopped item: {stack.pop()}") # Should pop Misa

stack.display()
# Output order from top to bottom: Hieu -> Thai