# ANALOGY: The blueprint for a Doubly Linked List friend.
# Each friend knows their own name, a paper pointing forward (next),
# and a paper pointing backward (prev).
class FriendNode:
    def __init__(self, name):
        self.data = name
        self.next: FriendNode | None = None  # Slip of paper pointing to the friend in front
        self.prev: FriendNode | None = None  # Slip of paper pointing to the friend behind


# ANALOGY: The manager of the two-way line.
class DoublyFriendsLine:
    def __init__(self):
        self.head: FriendNode | None = None  # Front of the line
        self.tail: FriendNode | None = None  # Back of the line

    # -------------------------------------------------------------
    # OPERATION: INSERTION (Squeezing Matthew in between two friends)
    # -------------------------------------------------------------
    def insert_after(self, left_friend, new_friend_name):
        if left_friend is None:
            return

        # Create our new friend node
        new_friend = FriendNode(new_friend_name)
        
        # ANALOGY STEP 1: Matthew sets his own forward paper to point to whoever 
        # was standing in front of left_friend.
        new_friend.next = left_friend.next
        
        # ANALOGY STEP 2: Matthew sets his own backward paper to point directly to left_friend.
        new_friend.prev = left_friend

        # ANALOGY STEP 3: If there actually is someone in front of Matthew,
        # that person must look backward and point their paper at Matthew.
        if left_friend.next is not None:
            left_friend.next.prev = new_friend
        else:
            # If nobody was in front, Matthew is now the end of the line (tail)
            self.tail = new_friend

        # ANALOGY STEP 4: left_friend turns around and points their forward paper at Matthew.
        left_friend.next = new_friend

    # -------------------------------------------------------------
    # OPERATION: WALK FORWARD
    # -------------------------------------------------------------
    def walk_forward(self):
        current = self.head
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next
        print("End")

    # -------------------------------------------------------------
    # OPERATION: WALK BACKWARD
    # -------------------------------------------------------------
    def walk_backward(self):
        # ANALOGY: Start at the very back (tail) and use the 'prev' papers to walk backward.
        current = self.tail
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.prev
        print("Start")


# =================================================================
# GAMEPLAY: Connecting the friends two-ways
# =================================================================
thai = FriendNode("Thai")
hieu = FriendNode("Hieu")
misa = FriendNode("Misa")

line = DoublyFriendsLine()
line.head = thai
line.tail = misa

# Connect Thai <-> Hieu
thai.next = hieu
hieu.prev = thai

# Connect Hieu <-> Misa
hieu.next = misa
misa.prev = hieu

print("--- Walking Forward (Thai to Misa) ---")
line.walk_forward() # Thai <-> Hieu <-> Misa <-> End

# Squeeze Matthew in right after Hieu
line.insert_after(hieu, "Matthew")

print("\n--- Walking Backward after adding Matthew ---")
line.walk_backward() # Misa <-> Matthew <-> Hieu <-> Thai <-> Start