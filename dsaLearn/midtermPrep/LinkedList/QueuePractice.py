# #Singly LinkedList
# class FriendNode():
#     def __init__(self,name):
#         self.data = name
#         self.next: FriendNode | None = None

# #Create manager
# class FriendsLine():
#     def __init__(self):
#         self.head: FriendNode | None = None

#     #method add friends
#     def addFriend(self, new_friend):
#         # Create the new friend node first
#         add_new_friend = FriendNode(new_friend)

#         if self.head == None:
#             self.head = add_new_friend
#         else:
#             current = self.head
#         # Keep stepping forward while the current person has a next neighbor
#             while current.next != None:
#                 current = current.next
#             current.next = add_new_friend

class FriendNode():
    def __init__(self,name):
        self.data = name
        self.next: FriendNode | None = None
        self.prev: FriendNode | None = None

class FriendsLine():
    def __init__(self):
        self.head: FriendNode | None = None
        self.tail: FriendNode | None = None

    def enqueue(self, name):
        # 1. Create a brand new person node. 
        # Both of their hands (next and prev) are currently holding nothing (None).
        new_friend = FriendNode(name)

        # 2. SCENARIO 1: The line is completely empty.
        if self.head is None or self.tail is None:
            # Since they are the only person here, they are simultaneously 
            # the front (head) and the back (tail) of the line.
            self.head = new_friend
            self.tail = new_friend
            return

        # 3. SCENARIO 2: There are already people in the line.
        # Let's attach the newcomer to the person currently at the very back (self.tail).
        
        # Step A: Tell the current last person to reach out their RIGHT hand (next)
        # and hold hands with the new friend.
        self.tail.next = new_friend  

        # Step B: Tell the new friend to reach out their LEFT hand (prev)
        # and hold hands with that old last person.
        new_friend.prev = self.tail  

        # Step C: The chain is now linked! Finally, the manager updates their records
        # to declare that this new friend is officially the new back of the line.
        self.tail = new_friend

    def dequeue(self):
        # 1. SCENARIO 1: The line is already empty.
        if self.head is None:
            return None # Nothing to remove

        # 2. Save the front person's name so we can return it at the end.
        leaving_friend = self.head.data

        # 3. SCENARIO 2: There is only ONE person in the entire line.
        if self.head == self.tail:
            # If they leave, the line becomes completely empty.
            self.head = None
            self.tail = None
            return leaving_friend

        # 4. SCENARIO 3: There are multiple people in line.
        # Step A: Move the manager's 'head' marker to the second person in line.
        self.head = self.head.next  

        # Step B: Tell this new front person to let go of their LEFT hand (prev).
        # Since the old front person left, nobody is standing ahead of them anymore.
        if self.head is not None:
            self.head.prev = None       

        # 5. Return the name of the person who just got their coffee and left.
        return leaving_friend
    
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
    
# --- FIXED TESTING BLOCK ---
line = FriendsLine()

# Use enqueue so both next, prev, and tail pointers are built automatically
line.enqueue("Thai")
line.enqueue("Hieu")
line.enqueue("Misa")
line.enqueue("Jimmy")

print("--- Original Friends Line ---")
line.display() 
# Output: Thai <-> Hieu <-> Misa <-> Jimmy <-> None

print("\n--- Enqueue Martin ---")
line.enqueue("Martin")
line.display() 
# Output: Thai <-> Hieu <-> Misa <-> Jimmy <-> Martin <-> None

print("\n--- Dequeue Someone ---")
removed = line.dequeue()
print(f"{removed} left the line.")
line.display()
# Output: Hieu <-> Misa <-> Jimmy <-> Martin <-> None