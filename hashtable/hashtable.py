import sys

sys.path.append("../hashtable/linked_list")
from linked_list import LinkedList


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

        self.storage = [LinkedList()] * capacity
        self.count = 0

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
        return self.count / self.capacity

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
        current = self.storage[index].head
        while current:
            if current.key == key:
                current.value = value
            current = current.next

        node = HashTableEntry(key, value)
        self.storage[index].insert_at_head(node)
        self.count += 1

        # init linked list at index position
        # if collision -> reassign to either head or tail

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # this probably deletes the entire linked list, refactor to empty linked list or check for none

        import math

        load = self.get_load_factor()
        if load < 0.2:
            current_capacity = self.get_num_slots()
            new_capacity = math.ceil(current_capacity * 0.5)
            if new_capacity < MIN_CAPACITY:
                new_capacity = MIN_CAPACITY
            self.resize(new_capacity)

        index = self.hash_index(key)
        current = self.storage[index].head

        if key:
            while current:
                if current.key == key:
                    current.value = None
                current = current.next
        else:
            print("key not found")

        # if key:
        #     # like in put need a while loop to match the keys
        #     # set value to None
        #     # update capacity
        #     index = self.hash_index(key)
        #     self.storage[index] = None
        #     self.count -= 1

        # else:
        #     print("key not found")
        # # add print warning if key not found

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        current = self.storage[index].head
        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # copy "old" storage to variable
        # hint: just a few lines of code
        # init empty [LinkedList()] * "new_capacity"
        # for each LL in old array -> nested while loop (if next node? copy / paste all nodes)
        # update count
        # if < get_load_size (0.7) then call resize func (use in put and delete functions)
        self.capacity = new_capacity
        new_storage = [None] * new_capacity

        for i in self.storage:
            if i is not None:
                current = i.head
                while current is not None:
                    a = self.hash_index(current.key)
                    if new_storage[a] is None:
                        linked = LinkedList()
                        linked.head = current
                        new_storage[a] = linked
                    else:
                        new_storage[a].insert_at_head(current)
                    current = current.next
        self.storage = new_storage
        return


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
