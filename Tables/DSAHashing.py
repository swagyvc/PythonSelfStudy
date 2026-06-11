class HashTable:
    def __init__(self, size=10):
        # Create an array of empty lists (buckets) to handle chaining
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        # A simple modulo hash function using Python's built-in hash()
        return abs(hash(key)) % self.size

    def insert(self, key, value):
        # Find the targeted index bucket
        index = self._hash_function(key)
        bucket = self.table[index]
        
        # Check if key already exists to update it
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # If key is completely new, append it to the bucket list
        bucket.append((key, value))

    def get(self, key):
        # Find the index bucket
        index = self._hash_function(key)
        bucket = self.table[index]
        
        # Search sequentially through the linked bucket
        for k, v in bucket:
            if k == key:
                return v
        return None # Key not found

    def delete(self, key):
        index = self._hash_function(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False
