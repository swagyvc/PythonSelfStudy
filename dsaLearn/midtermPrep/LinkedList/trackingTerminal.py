class Node:
    def __init__(self, timestamp):
        self.timestamp = timestamp
        self.next: Node | None = None

class RequestTracker:
    def __init__(self, max_size=5):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.current_size = 0
        self.max_size = max_size

    def log_request(self, timestamp):
        new_node = Node(timestamp)

        # If list is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.current_size += 1
            return

        # Append to the tail (O(1))
        self.tail.next = new_node
        self.tail = new_node
        self.current_size += 1

        # If we exceed the max size, evict the oldest from the head (O(1))
        if self.current_size > self.max_size:
            self.head = self.head.next
            self.current_size -= 1

    def display_log(self):
        current = self.head
        log_items = []
        while current:
            log_items.append(str(current.timestamp))
            current = current.next
        print("Oldest -> " + " -> ".join(log_items) + " -> Newest")

# --- Test Execution ---
if __name__ == "__main__":
    tracker = RequestTracker(max_size=3) # Track only the last 3 requests
    
    print("User makes 3 requests:")
    tracker.log_request("10:00:01")
    tracker.log_request("10:00:02")
    tracker.log_request("10:00:03")
    tracker.display_log()

    print("\nUser makes a 4th request (Oldest should drop instantly):")
    tracker.log_request("10:00:04")
    tracker.display_log()