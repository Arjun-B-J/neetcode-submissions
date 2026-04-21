class Node:
    def __init__(self,val,nextNode):
        self.val = val
        self.nextNode = nextNode

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        cur = self.head
        i = 0
        while(i<index and cur is not None):
            cur = cur.nextNode
            i+=1
        if cur is None:
            return -1
        return cur.val  
        

    def insertHead(self, val: int) -> None:
        if(self.head == None):
            newNode = Node(val,None)
            self.head = newNode
            self.tail = newNode
        else:
            newNode = Node(val,self.head)
            self.head = newNode
        

    def insertTail(self, val: int) -> None:
        if(self.head==None):
            newNode = Node(val,None)
            self.head = newNode
            self.tail = newNode
        else:
            newNode = Node(val,None)
            self.tail.nextNode = newNode
            self.tail = newNode
        

    def remove(self, index: int) -> bool:
        cur = self.head
        if cur is None:
            return False
        currentIndex = 0
        
        if(index == 0):
            if(self.head == self.tail):
                self.head = None
                self.tail = None
                return True
            self.head = self.head.nextNode
            return True

        while( cur is not None and currentIndex < index):
            if(currentIndex == index-1):
                if(cur.nextNode and self.tail == cur.nextNode):
                    self.tail = cur
                if(cur.nextNode):
                    cur.nextNode = cur.nextNode.nextNode
                    return True
                else:
                    return False
            cur = cur.nextNode
            currentIndex +=1
        return False

           
        

    def getValues(self) -> List[int]:
        cur = self.head
        ans = []
        while(cur):
            ans.append(cur.val)
            cur = cur.nextNode
        return ans
        
