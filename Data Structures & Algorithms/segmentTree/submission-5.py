class SegmentNode:
    def __init__(self,total,L,R):
        self.total = total
        self.L = L
        self.R = R
        self.right = None
        self.left = None

class SegmentTree:

    def build(self,nums,L,R):
        if L==R:
            return SegmentNode(nums[L],L,R)
        M = (L+R)//2
        root = SegmentNode(0,L,R)
        root.left = self.build(nums,L,M)
        root.right = self.build(nums,M+1,R)
        root.total = root.left.total + root.right.total
        return root 

    def __init__(self, nums: List[int]):
        self.root = self.build(nums,0,len(nums)-1)
    
    def updateTree(self,root,index,val):
        if root.L==root.R:
            root.total = val
            return
        M = (root.L+root.R)//2
        if index>M:
            self.updateTree(root.right,index,val)
        else:
            self.updateTree(root.left,index,val)
        root.total = root.right.total + root.left.total

    def update(self, index: int, val: int)->None:
        self.updateTree(self.root,index,val)
        
    def queryTree(self,root,L,R):
        if root.L == L and root.R == R:
            return root.total
        M = (root.L+root.R)//2
        if L>M:
            return self.queryTree(root.right,L,R)
        elif R<=M:
            return self.queryTree(root.left,L,R)
        else:
            return self.queryTree(root.left,L,M) + self.queryTree(root.right,M+1,R)

    
    def query(self, L: int, R: int) -> int:
        return self.queryTree(self.root,L,R)

