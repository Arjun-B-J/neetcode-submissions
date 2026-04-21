# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:return True #empty subtree
        if not root:return False #empty root and there is a subtree, we return False
        if self.sameTree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        

    def sameTree(self,p,q):
        if not p and not q:#if both are null then its true
            return True
        if p and q and p.val==q.val: # both there and equal nodes, recursively check left and right
            return self.sameTree(p.left,q.left) and self.sameTree(p.right,q.right)
        return False # one there and one not there cases