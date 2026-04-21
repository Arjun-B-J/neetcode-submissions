class Node:
    def __init__(self,v,n=None):
        self.v = v
        self.n = n
class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
    
    def get(self, index: int) -> int:
        i = 0
        cur = self.head.n
        while(cur and i<index):
            i+=1
            cur = cur.n
        return cur.v if cur else -1

    def insertHead(self, val: int) -> None:
        nN = Node(val,self.head.n)
        if self.head.n is None:
            self.tail = nN
        self.head.n = nN

    def insertTail(self, val: int) -> None:
        self.tail.n = Node(val)
        self.tail = self.tail.n
        if self.head.n is None:
            self.head.n = self.tail

    def remove(self, index: int) -> bool:
        i = 0
        cur = self.head
        while(cur and i<index):
            i+=1
            cur = cur.n
        if(cur and cur.n):
            if self.tail == cur.n:
                self.tail = cur
            cur.n = cur.n.n
            return True
        return False

    def getValues(self) -> List[int]:
        ans = []
        cur = self.head.n
        while(cur):
            ans.append(cur.v)
            cur = cur.n
        return ans
        
