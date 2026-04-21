class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.left , self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self,node):
        prev,next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    def insert(self,node):
        prev,next = self.right.prev,self.right
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            ans = self.cache[key]
            self.remove(ans)
            self.insert(ans)
            return ans.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return
        newNode = Node(key,value)
        self.insert(newNode)
        self.cache[key] = newNode
        if len(self.cache) > self.capacity:
            LRU = self.left.next
            del self.cache[LRU.key]
            self.remove(LRU)
       