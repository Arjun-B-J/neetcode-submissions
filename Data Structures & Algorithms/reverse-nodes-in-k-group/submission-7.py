# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            # 1. Find the kth node from groupPrev
            kth = self.getKth(groupPrev, k)
            if not kth:
                break # Not enough nodes left to reverse
                
            groupNext = kth.next
            
            # 2. Reverse the group
            prev, curr = kth.next, groupPrev.next # Clever trick: initialize prev to groupNext
            
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                
            # 3. Update the connections to link the reversed group back to the main list
            temp = groupPrev.next # This is the old head, now the tail of the group
            groupPrev.next = kth  # Link previous part to the new head (kth)
            groupPrev = temp      # Move groupPrev forward for the next iteration
            
        return dummy.next

    # Helper function to clearly find the end of our k-group
    def getKth(self, curr: ListNode, k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr