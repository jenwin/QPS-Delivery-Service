# Hashtable

# A. HashTable class with chaining
class HashTable:

    # A function that contains initial capacity of 35
    def __init__(self, initial_capacity=35):
        # Assigns the initial_capacity to capacity attribute
        self.capacity = initial_capacity
        # Assigns all buckets with an empty list in the hash table
        self.table = [[] for _ in range(self.capacity)]

    # Insertion and update function, inserts a new item into the hash table
    def insert_package(self, key, item):
        # Gets the hash key where the item will go into the bucket
        bucket = hash(key) % self.capacity
        # Access the hash table with the hash key, assigns to bucket_list
        bucket_list = self.table[bucket]

        # The key is updated if it exists in the bucket
        for kv in bucket_list:
            # Checks if the key is equal to the searched key
            if kv[0] == key:
                # If the key is equal to the searched key, it updates the value to the item
                kv[1] = item
                # Returns true if updated
                return True

        # The key value pair that will be added
        key_value = [key, item]
        # Adds the key value pair to the end of the bucket list
        bucket_list.append(key_value)
        # Returns true if it successfully adds the key, item
        return True

    # LOOKUP FUNCTION
    # Looks up items in the hash table
    def lookup_package(self, key):
        # Gets the hash key where the item will go into the bucket
        bucket = hash(key) % self.capacity
        # Access the hash table with the hash key, assigns to bucket_list
        bucket_list = self.table[bucket]

        # Loops through the bucket_list with kv
        for kv in bucket_list:
            # Checks if the key matches any keys
            if kv[0] == key:
                # Returns the value from the key value pair
                return kv[1]
        # If the key does not match the searched key, it returns None (not found)
        return None

    # Remove function
    def remove(self, key):
        # Get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        # Access the hash table with the hash key, assigns to bucket_list
        bucket_list = self.table[bucket]

        # Remove the item from the bucket list if it is present.
        for kv in bucket_list:
            # Checks if the key matches any keys
            if kv[0] == key:
                # If it matches, remove it
                bucket_list.remove([kv[0], kv[1]])


# Create a hash_table instance from HashTable class
hash_table = HashTable()
