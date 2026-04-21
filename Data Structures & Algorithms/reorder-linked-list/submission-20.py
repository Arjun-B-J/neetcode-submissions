# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None
            
        # 1. Find the middle
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 2. Reverse the second half
        cur = slow.next
        slow.next = None  # CRITICAL FIX: Split the two halves!
        
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            
        # 3. Merge the two halves
        left = head
        right = prev
        
        # We only need to check 'right' because it will always be 
        # equal to or one node shorter than 'left'.
        while right:
            # Temporarily store the next nodes
            temp_left = left.next
            temp_right = right.next
            
            # Re-wire the pointers: left -> right -> temp_left
            left.next = right
            right.next = temp_left
            
            # Move the left and right pointers forward
            left = temp_left
            right = temp_right