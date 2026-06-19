```py
# 1. THE BUILDING BLOCK (The Node)
class Node:
    def __init__(self, data):
        self.data = data  # Stores the actual value
        self.next = None  # Stores the address of the next node (None means end of list)


# 2. THE MANAGER (The Linked List structure)
class SinglyLinkedList:
    def __init__(self):
        self.head = None  # The entry point of the list. Initially empty.

    # INSERT AT THE VERY FRONT (Changing the head)
    def insert_at_front(self, new_data):
        new_node = Node(new_data)  # Step 1: Create the new clue box
        new_node.next = self.head  # Step 2: Point new node's string to the current first node
        self.head = new_node       # Step 3: Move the main entrance marker to our new node

    # INSERT IN THE MIDDLE (After a specific node)
    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            return  # Can't insert after a node that doesn't exist

        new_node = Node(new_data)       # Step 1: Create the new node
        new_node.next = prev_node.next  # Step 2: Tie new node to the back half of the list FIRST
        prev_node.next = new_node       # Step 3: Tie the front half to the new node second

    # DELETE A NODE BY VALUE
    def delete_value(self, target):
        current = self.head
        prev = None

        # Case A: The list is completely empty
        if current is None:
            return

        # Case B: The node to delete is the very first node (the Head)
        if current.data == target:
            self.head = current.next  # Bypass the head by making the second node the new head
            return

        # Case C: Search for the target in the middle/end of the list
        while current is not None and current.data != target:
            prev = current          # Keep track of the node right behind us
            current = current.next  # Step forward down the chain

        # If we reached the end (None) and never found the target
        if current is None:
            return

        # Perform the bypass: link the previous node straight to the target's next node
        prev.next = current.next

    # TRAVERSE AND PRINT (The Golden Rule)
    def display(self):
        # ALWAYS use a temporary runner variable ('current') so you don't destroy self.head
        current = self.head
        
        # Keep walking forward until you fall off the end of the list into None
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next  # Follow the pointer to the next node
        print("None")


# ==========================================
# EXAM SIMULATION: How to use it
# ==========================================
# Constructing: [Apple] -> [Banana] -> [Cherry]
my_list = SinglyLinkedList()
my_list.insert_at_front("Banana")
my_list.insert_at_front("Apple")  # Apple is now the head

# Let's target the head node to insert 'Cherry' right after 'Banana'
banana_node = my_list.head.next
my_list.insert_after(banana_node, "Cherry")

my_list.display()  # Output: Apple -> Banana -> Cherry -> None

# Delete the middle node
my_list.delete_value("Banana")
my_list.display()  # Output: Apple -> Cherry -> None
```

Let's take our line of people (**Amy**, **Ben**, and **Cal**) and map them directly to the code terms.

Here is exactly how the analogy translates to a Singly Linked List:

---

### 1. The Blueprint (`class Node`)

Each person in our line is an object of the `Node` class. Inside their pockets, they hold two variables:

* `self.data` = The actual person's name (e.g., `"Amy"`).
* `self.next` = The piece of paper pointing to the next person.

```python
# The blueprint for making an Amy, a Ben, or a Cal
class Node:
    def __init__(self, data):
        self.data = data  # The name string
        self.next = None  # The slip of paper (starts blank)

```

---

### 2. Creating the People

When we instantiate the nodes, we are just spawning three independent people in the room. Right now, their `next` papers are blank (`None`). They don't know each other yet.

```python
amy = Node("Amy")
ben = Node("Ben")
cal = Node("Cal")

```

---

### 3. Tying the Chain Together

To make a list, we write on their papers to link them up.

```python
amy.next = ben  # On Amy's paper, we write "Ben"
ben.next = cal  # On Ben's paper, we write "Cal"
# cal.next stays None because nobody is behind him

```

---

### 4. Setting up the Entrance (`self.head`)

The `SinglyLinkedList` class is just the manager of the game. It holds the main entrance arrow called `head`. We point it at Amy because she is first.

```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Line starts empty

# Start the game by pointing the entrance at Amy
my_list = SinglyLinkedList()
my_list.head = amy 

```

---

### 5. Walking the Line (`print_list`)

When you want to print the list, you create a temporary runner variable called `current`. Think of `current` as **you** physically walking down the line.

```python
# You start your walk at the entrance sign
current = my_list.head  # current is now looking at Amy

while current is not None:
    print(current.data)       # You read the person's nametag
    current = current.next    # You read their paper and move to that next person!

```

* **Loop Step 1:** `current` is Amy. Prints `"Amy"`. Updates `current` to Amy's next (`ben`).
* **Loop Step 2:** `current` is Ben. Prints `"Ben"`. Updates `current` to Ben's next (`cal`).
* **Loop Step 3:** `current` is Cal. Prints `"Cal"`. Updates `current` to Cal's next (`None`).
* **Loop Step 4:** `current` is now `None`. The `while` loop sees `None` and safely stops.