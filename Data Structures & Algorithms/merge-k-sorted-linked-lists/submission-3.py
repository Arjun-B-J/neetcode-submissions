# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self,L,R):
        ansHead = None
        cur = None
        while(L and R):
            if L.val <= R.val:
                newNode = ListNode(L.val)
                if ansHead is None:
                    ansHead = newNode
                    cur = newNode
                    L=L.next
                    continue
                cur.next = newNode
                cur = newNode
                L = L.next
            else:
                newNode = ListNode(R.val)
                if ansHead is None:
                    ansHead = newNode
                    cur = newNode
                    R=R.next
                    continue
                cur.next = newNode
                cur = newNode
                R= R.next
        while(L):
            newNode = ListNode(L.val)
            if ansHead is None:
                ansHead = newNode
                cur = newNode
                L=L.next
                continue
            cur.next = newNode
            cur = newNode
            L = L.next
        while(R):
            newNode = ListNode(R.val)
            if ansHead is None:
                ansHead = newNode
                cur = newNode
                R=R.next
                continue
            cur.next = newNode
            cur = newNode
            R = R.next
        return ansHead

        
    def mS(self,lists,s,e):
        if e-s+1 <= 1:
            return lists[s]
        m = (s+e)//2
        L = self.mS(lists,s,m)
        R = self.mS(lists,m+1,e)
        return self.merge(L,R)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists)==0:
            return None
        return self.mS(lists,0,len(lists)-1)        