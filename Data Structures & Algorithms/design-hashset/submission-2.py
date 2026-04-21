# Time Complexity: O(1) average case for all operations. O(N) worst case if all elements hash to the exact same bucket (rare).
# Space Complexity: O(K + M) where K is the number of added elements and M is the number of predefined buckets.
# Approach: Separate Chaining (Array of Linked Lists)

class ListNode:
    def __init__(self, key=-1, next=None):
        self.key = key
        self.next = next

class MyHashSet:
    def __init__(self):
        # We choose a relatively large prime-ish number for our bucket array size.
        # This helps distribute the keys evenly to minimize collisions.
        self.size = 10000
        
        # Initialize an array of dummy nodes. 
        # Dummy nodes make adding/removing from the head of the linked list much easier!
        self.buckets = [ListNode() for _ in range(self.size)]
        
    def _hash(self, key: int) -> int:
        # Our custom hash function. Maps any key to an index between 0 and 9999.
        return key % self.size

    def add(self, key: int) -> None:
        curr = self.buckets[self._hash(key)]
        
        # Traverse the linked list at this bucket
        while curr.next:
            if curr.next.key == key:
                return  # Key already exists, do nothing
            curr = curr.next
            
        # If we reached the end and didn't find the key, append it
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        curr = self.buckets[self._hash(key)]
        
        # Traverse looking for the key to remove
        while curr.next:
            if curr.next.key == key:
                # Bypass the node to delete it
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        curr = self.buckets[self._hash(key)]
        
        # Traverse looking for a match
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
            
        return False