# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        
        slow = dummy
        fast = dummy
        
        # Step 1: Give 'fast' a head start of n steps
        for _ in range(n):
            fast = fast.next
            
        # Step 2: Move both until 'fast' reaches the LAST node
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        # Step 3: 'slow' is now right before the node we want to delete
        slow.next = slow.next.next
        
        return dummy.next