# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ans = None
    mainK = None
    def inOrder(self,root):
        if root is None or self.mainK ==0:
            return
        self.inOrder(root.left)
        if(self.mainK == 1):
            self.ans = root.val
            self.mainK=0
        else:
            self.mainK-=1
        self.inOrder(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return None
        self.mainK = k
        self.inOrder(root)
        return self.ans if self.ans else 0