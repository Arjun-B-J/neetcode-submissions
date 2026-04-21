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
        cur = head
        cloneHead = Node(-1)
        cloneCur = cloneHead
        i=0
        map = {} 
        while cur: #i am copying the nodes here
            cloneCur.next = Node(cur.val)
            map[cur] = cloneCur.next #maps cur node to the new node
            cloneCur=cloneCur.next
            cur=cur.next

        cur = head
        cloneCur = cloneHead.next
        while cur: #setting the random for the new nodes
            print(cur.val)
            if cur.random:
                cloneCur.random = map[cur.random]
            else:
                cloneCur.random = None
            cloneCur=cloneCur.next
            cur = cur.next
        return cloneHead.next