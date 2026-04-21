class Node:
    def __init__(self,key,val,left = None, right = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:   
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = Node(key,val)
        if not self.root:
            self.root = newNode
            return
        cur = self.root
        while True:
            if cur.key < key:
                if not cur.right:
                    cur.right = newNode
                    return
                cur = cur.right
            elif cur.key > key:
                if not cur.left:
                    cur.left = newNode
                    return
                cur = cur.left
            else:
                cur.val = val
                return

    def get(self, key: int) -> int:
        if not self.root:
            return -1
        cur = self.root
        while(cur):
            if key>cur.key:
                cur = cur.right
            elif key<cur.key:
                cur = cur.left
            else:
                return cur.val
        return -1


    def getMin(self) -> int:
        if not self.root:
            return -1
        cur = self.root
        while(cur and cur.left):
            cur = cur.left
        return cur.val


    def getMax(self) -> int:
        if not self.root:
            return -1
        cur = self.root
        while(cur and cur.right):
            cur = cur.right
        return cur.val

    def findMin(self,root) -> Node:
        cur = root
        while(cur and cur.left):
            cur = cur.left
        return cur

    def removeHelper(self,cur,key) -> Node:
        if not cur:
            return None
        if key > cur.key:
            cur.right = self.removeHelper(cur.right,key)
        elif key < cur.key:
            cur.left = self.removeHelper(cur.left,key)
        else:
            if not cur.left:
                return cur.right
            if not cur.right:
                return cur.left
            minNode = self.findMin(cur.right)
            cur.key = minNode.key
            cur.val = minNode.val
            cur.right = self.removeHelper(cur.right,minNode.key)
        return cur


    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root,key)

    def inOrderTraversal(self,root,ans):
        if not root:
            return
        self.inOrderTraversal(root.left,ans)
        ans.append(root.key)
        self.inOrderTraversal(root.right,ans)

    def getInorderKeys(self) -> List[int]:
        if not self.root:
            return []
        ans = []
        self.inOrderTraversal(self.root,ans)
        return ans

