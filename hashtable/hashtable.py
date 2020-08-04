class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        # self.capacity = capacity
        # initialize empty list? [None] * MIN_CAPACITY
        # self.data = [None] * MIN_CAPACITY
        # capacity param is if user sets capacity else default to min
        if capacity > MIN_CAPACITY:
            self.capacity = capacity

        else:
            self.capacity = MIN_CAPACITY

        self.storage = [None] * capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # pass
        # length of list is the capacity?
        # return capacity?
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # load factor = # of items in hash table / total # of slots (capacity)
        pass

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        self.fnv_prime = 1099511628211
        self.hash = 14695981039346656037

        for character in key:
            self.hash = self.hash * self.fnv_prime
            self.hash = self.hash ^ ord(character)

        return self.hash
        # FNV_offset_basis = 14695981039346656037
        # FNV_prime = 1099511628211

        # hashed_var = FNV_offset_basis

        # string_bytes = s.encode()

        # for b in string_bytes:
        #     hashed_var = hashed_var * FNV_prime
        #     hashed_var = hashed_var ^ b
        # return hashed_var

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # 5381 & 33 are prime numbers
        # hashed_var = 5381

        # string_bytes = s.encode()

        # for b in string_bytes:
        #     hash_var = ((hash_var << 5) + hash_var) + b

        # return hash_var

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        self.storage[index] = value

        # init linked list at index position
        # if collision -> reassign to either head or tail

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        if key:

            index = self.hash_index(key)
            self.storage[index] = None

        else:
            print("key not found")
        # add print warning if key not found

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        return self.storage[index]

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        pass


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
