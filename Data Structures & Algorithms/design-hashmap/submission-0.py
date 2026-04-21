# ==========================================
# Approach 1: Separate Chaining (Array of Linked Lists)
# Time Complexity: O(1) average case. O(N) worst case if there are many collisions.
# Space Complexity: O(K + M) where K is added elements and M is the bucket size.
# ==========================================
class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val  # Only difference from HashSet: We store a value!
        self.next = next

class MyHashMap:
    def __init__(self):
        # A prime-ish bucket size to distribute keys evenly
        self.size = 10000
        # Initialize array with dummy nodes for easier linked list management
        self.buckets = [ListNode() for _ in range(self.size)]
        
    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        curr = self.buckets[self._hash(key)]
        
        while curr.next:
            if curr.next.key == key:
                # Key already exists, UPDATE the value!
                curr.next.val = value
                return
            curr = curr.next
            
        # Key does not exist, APPEND it to the end
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        curr = self.buckets[self._hash(key)]
        
        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
            
        # Problem asks us to return -1 if the key doesn't exist
        return -1

    def remove(self, key: int) -> None:
        curr = self.buckets[self._hash(key)]
        
        while curr.next:
            if curr.next.key == key:
                # Bypass the node to delete it
                curr.next = curr.next.next
                return
            curr = curr.next