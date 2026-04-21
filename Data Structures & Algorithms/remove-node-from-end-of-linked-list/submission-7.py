# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=1
        cur = head
        if not head:
            return None
        while cur:
            cur =cur.next
            l+=1
        indexToRemove = l-n
        tempHead = ListNode(-1)
        tempHead.next = head
        i=1
        cur=head
        while cur:
            
            if i==1 and indexToRemove==1:
                cur=cur.next
                tempHead.next=cur
                break
            if i==indexToRemove-1:
                print(i,cur.val,indexToRemove)
                cur.next=cur.next.next
                break
            i+=1
            cur=cur.next

        return tempHead.next
