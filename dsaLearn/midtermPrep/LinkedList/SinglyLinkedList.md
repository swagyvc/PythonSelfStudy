```python
# ANALOGY: The Blueprints for a Clue Box
# Each clue box holds an item (data) and a slip of paper pointing to the next location (next).
class Node:
    def __init__(self, data):
        self.data = data    # The prize/value inside this specific box
        self.next = None    # The map/string pointing to the next box (starts unlinked)

class SinglyLinkedList:
    def __init__(self):
        self.head = None    # ANALOGY: The very first clue location. If None, the hunt hasn't started.

    # ==========================================
    # OPERATION 1: TRAVERSAL (Walking the list)
    # ==========================================
    def print_list(self):
        # ANALOGY: Start your hunt at the front door (the Head)
        current = self.head
        
        # ANALOGY: Keep following clues until you find a blank slip of paper (None)
        while current is not None:
            print(current.data)       # Read the current clue/data
            current = current.next    # Follow the string to the next box!
            
    # ==========================================
    # OPERATION 2: INSERTION (Adding to the middle)
    # ==========================================
    def insert_after_node(self, prev_node, new_data):
        if prev_node is None:
            print("The previous node must exist.")
            return

        # ANALOGY: Create a brand new person who wants to jump into a Conga Line
        new_node = Node(new_data)
        
        # ANALOGY STEP 1: New person places their hands on the waist of the person ahead
        new_node.next = prev_node.next
        
        # ANALOGY STEP 2: The person behind lets go of their old target and grabs the new person
        prev_node.next = new_node

    # ==========================================
    # OPERATION 3: DELETION (Removing from the middle)
    # ==========================================
    def delete_by_value(self, target_value):
        current = self.head
        prev = None

        # Special Case: If the very first clue box is the one we want to destroy
        if current is not None and current.data == target_value:
            self.head = current.next # Move the front door marker to the second box
            return

        # ANALOGY: Walk down the chain to find the target, keeping track of the person behind them (prev)
        while current is not None and current.data != target_value:
            prev = current
            current = current.next

        # If the value wasn't found in the list
        if current is None:
            return

        # ANALOGY: "Ghosting" the target. The person behind (prev) completely bypasses 
        # the current target and ties their string straight to the person after them (current.next).
        prev.next = current.next


# ==========================================
# TESTING THE CHAIN
# ==========================================
# 1. Setup the initial list: Dick -> Harry -> Tom
llist = SinglyLinkedList()
llist.head = Node("Dick")
node_2 = Node("Harry")
node_3 = Node("Tom")

llist.head.next = node_2  # Dick points to Harry
node_2.next = node_3      # Harry points to Tom

print("--- Original List ---")
llist.print_list()

# 2. Delete Harry (The middle node)
llist.delete_by_value("Harry")

print("\n--- After Deleting Harry ---")
llist.print_list() # Outputs: Dick, Tom
```