# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBST(left,root,right):
            if not root:
                return True
            if not (left<root.val<right): # if this breaks return False
                return False # update right when going left and vice versa
            return isBST(left,root.left,root.val) and isBST(root.val,root.right,right)
        return isBST(float("-inf"),root,float("inf")) #we give left and right initially as + and - inf