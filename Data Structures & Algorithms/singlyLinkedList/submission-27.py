class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
    
    def get(self, index: int) -> int:
        cur = self.head.next
        i = 0
        while(cur and i<index):
            cur=cur.next
            i+=1
        return cur.val if cur else -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val,self.head.next)
        if self.head.next is None:
            self.tail = newNode
        self.head.next = newNode

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next
        if self.head.next is None:
            self.head.next = self.tail

    def remove(self, index: int) -> bool:
        i = 0
        cur = self.head
        while(i<index and cur):
            cur = cur.next
            i+=1
        if cur and cur.next:
            if self.tail == cur.next:
                self.tail = cur
            cur.next = cur.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        vals = []
        cur = self.head.next
        while(cur):
            vals.append(cur.val)
            cur = cur.next
        return vals
