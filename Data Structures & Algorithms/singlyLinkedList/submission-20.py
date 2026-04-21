class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
    
    def get(self, index: int) -> int:
        i = 0
        cur = self.head.next
        while(cur and i<index):
            i+=1
            cur = cur.next
        if cur:
            return cur.val
        else:
            return -1
        

    def insertHead(self, val: int) -> None:
        newNode = Node(val,self.head.next)
        if self.head.next is None:
            self.tail = newNode
        self.head.next = newNode

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        self.tail.next = newNode
        self.tail = newNode
        if not self.head.next:
            self.head.next = newNode
        

    def remove(self, index: int) -> bool:
        i = 0
        cur = self.head
        while(i<index and cur):
            i+=1
            cur=cur.next
        if cur and cur.next:
            if(self.tail == cur.next):
                self.tail = cur
            cur.next= cur.next.next
            return True
        else:
            return False

    def getValues(self) -> List[int]:
        cur = self.head.next
        vals = []
        while(cur):
            vals.append(cur.val)
            cur = cur.next
        return vals
        
