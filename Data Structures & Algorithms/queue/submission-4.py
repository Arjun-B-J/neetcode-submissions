class Node:
    def __init__(self,val):
        self.val=val
        self.next = None
        self.prev = None
class Deque:
    
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next== self.tail

    def append(self, value: int) -> None:
        newNode = Node(value)
        prev,next = self.tail.prev,self.tail
        newNode.next = next
        newNode.prev = prev
        prev.next = newNode
        next.prev = newNode

    def appendleft(self, value: int) -> None:
        newNode = Node(value)
        prev,next = self.head,self.head.next
        newNode.next = next
        newNode.prev = prev
        prev.next = newNode
        next.prev = newNode
        
    def pop(self) -> int:
        if self.isEmpty():
            return -1
        popNode = self.tail.prev
        self.tail.prev = popNode.prev
        popNode.prev.next = self.tail
        return popNode.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        popNode = self.head.next
        self.head.next = popNode.next
        popNode.next.prev = self.head
        return popNode.val
        
