# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pathSum(self,root,path,targetSum):
        if not root:
            return False
        path.append(root.val)
        if not root.left and not root.right:
            if sum(path)==targetSum:
                return True
        if self.pathSum(root.left,path,targetSum):
            return True
        if self.pathSum(root.right,path,targetSum):
            return True
        path.pop()
        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.pathSum(root,[],targetSum)
        