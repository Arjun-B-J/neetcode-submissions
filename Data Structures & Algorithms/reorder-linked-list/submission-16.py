# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the mid we need 3
        # 1 2 3 4 5 6
        if not head:
            return None
        slow = head
        fast = head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #we at first mid if even or mid if odd
        prev = None
        next = None
        cur = slow.next #reverse the portion from the right 1 2 3     4 5 6
        temp = None
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        
        left = head
        cur = left
        right=prev
        i=1
        while cur and left or right:
            if i%2==0:
                temp=right.next
                cur.next = left
                cur=cur.next
                right =temp
                i+=1
            else:
                temp=left.next  
                cur.next = right
                cur = cur.next
                left = temp
                i+=1
        if cur:
            cur.next = left or right
        return None








