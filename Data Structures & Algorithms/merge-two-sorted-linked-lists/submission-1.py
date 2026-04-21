# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        cur = None
        prev = None
        while(list1 and list2):
            if list1.val < list2.val:
                cur = list1
                list1=list1.next
            else:
                cur = list2
                list2 = list2.next
            if prev:
                prev.next = cur
                prev = cur
            else:
                prev = cur
            if head is None:
                head = cur
        if list1:
            if prev is None:
                return list1
            prev.next = list1
        if list2:
            if prev is None:
                return list2
            prev.next = list2
        return head
