class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
class LinkedList:
    
    def __init__(self):
        self.head = Node(10)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        cur = self.head.next
        i=0
        while(cur and i<index):
            cur = cur.next
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
        while(cur and i<index):
            i+=1
            cur=cur.next
        if cur and cur.next:
            if self.tail == cur.next:
                self.tail = cur
            cur.next = cur.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        ans = []
        cur = self.head.next
        while(cur):
            ans.append(cur.val)
            cur = cur.next
        return ans
        
