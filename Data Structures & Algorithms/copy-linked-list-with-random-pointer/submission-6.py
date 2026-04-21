"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        # Step 1: Interweave the cloned nodes
        curr = head
        while curr:
            # Create the clone and point it to the next original node
            new_node = Node(curr.val, curr.next)
            # Point the original node to the clone
            curr.next = new_node
            # Skip past the newly inserted clone to the next original node
            curr = new_node.next
            
        # Step 2: Assign random pointers for the clones
        curr = head
        while curr:
            if curr.random:
                # The clone's random is the original random's next node
                curr.next.random = curr.random.next
            # Jump to the next original node
            curr = curr.next.next
            
        # Step 3: Unweave the lists
        curr = head
        pseudo_head = Node(0, head.next) # Dummy head for the cloned list
        clone_curr = pseudo_head.next
        
        while curr:
            # Restore the original list
            curr.next = curr.next.next
            # Build the cloned list
            if clone_curr.next:
                clone_curr.next = clone_curr.next.next
                
            # Move both pointers forward
            curr = curr.next
            clone_curr = clone_curr.next
            
        return pseudo_head.next