# ANALOGY: The blueprint for an individual friend in the chain.
# Each friend knows their own name (data) and has a slip of paper 
# in their pocket pointing to the next friend in line (next).
class FriendNode:
    def __init__(self, name):
        self.data = name   # The friend's name (e.g., "Thai")
        self.next: FriendNode | None = None   # The slip of paper pointing to the next friend behind them


# ANALOGY: The manager of the group line.
class FriendsLine:
    def __init__(self):
        self.head: FriendNode | None = None   # The entrance marker. It points to whoever stands first in line.

    # -------------------------------------------------------------
    # OPERATION: WALK DOWN THE LINE
    # -------------------------------------------------------------
    def shout_out_names(self):
        # ANALOGY: We start walking from the very front of the line (the head).
        current = self.head
        
        # ANALOGY: Keep walking until you hit an empty space (None) where no one is standing.
        while current is not None:
            print(current.data, end=" -> ") # Read the current friend's nametag
            current = current.next           # Read their paper and step to the next friend
        print("End of Line")

    # -------------------------------------------------------------
    # OPERATION: INSERTION (Squeezing a friend into the middle)
    # -------------------------------------------------------------
    def insert_after_friend(self, front_friend, new_friend_name):
        # ANALOGY: Create a brand new friend (e.g., Matthew) who wants to join.
        new_friend = FriendNode(new_friend_name)
        
        # ANALOGY STEP 1: Matthew looks at front_friend's paper to see who used to be next,
        # and copies that onto his own paper. (Matthew now points to whoever is behind front_friend).
        new_friend.next = front_friend.next
        
        # ANALOGY STEP 2: front_friend erases their old paper and points it directly at Matthew.
        front_friend.next = new_friend


# =================================================================
# GAMEPLAY: Setting up our friends line
# =================================================================

# 1. Create the independent friend nodes
thai = FriendNode("Thai")
hieu = FriendNode("Hieu")
misa = FriendNode("Misa")
jimmy = FriendNode("Jimmy")

# 2. Setup the manager and point the entrance at Thai
line = FriendsLine()
line.head = thai  # Thai is officially the front of the line!

# 3. Connect them manually: Thai -> Hieu -> Misa -> Jimmy
thai.next = hieu   # Thai's pocket paper points to Hieu
hieu.next = misa   # Hieu's pocket paper points to Misa
misa.next = jimmy  # Misa's pocket paper points to Jimmy
# jimmy.next remains None because nobody is behind him yet

print("--- Original Friends Line ---")
line.shout_out_names() # Output: Thai -> Hieu -> Misa -> Jimmy -> End of Line

# 4. Matthew wants to squeeze in right after Hieu
print("\n--- Matthew squeezes in after Hieu ---")
line.insert_after_friend(hieu, "Matthew")

line.shout_out_names() # Output: Thai -> Hieu -> Matthew -> Misa -> Jimmy -> End of Line