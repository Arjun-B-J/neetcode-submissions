class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
    
    def get(self, index: int) -> int:
        i=0
        cur = self.head.next
        while(cur and i<index):
            i+=1
            cur=cur.next
        return cur.val if cur else -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val,self.head.next)
        if self.head.next is None:
            self.tail = newNode
        self.head.next = newNode

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        if self.head.next is None:
            self.head.next = newNode
        self.tail.next = newNode
        self.tail = newNode

    def remove(self, index: int) -> bool:
        i = 0
        cur = self.head
        while(cur and i<index):
            cur = cur.next
            i+=1
        if cur and cur.next:
            if self.tail == cur.next:
                self.tail = cur
            cur.next = cur.next.next
            return True
        else:
            return False

    def getValues(self) -> List[int]:
        values = []
        cur = self.head.next
        while(cur):
            values.append(cur.val)
            cur = cur.next
        return values
        
