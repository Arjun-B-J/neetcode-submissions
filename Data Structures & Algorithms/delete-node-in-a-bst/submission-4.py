# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMin(self,root: Optional[TreeNode]):
        cur = root
        while(cur and cur.left):
            cur = cur.left
        return cur
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            else:
                minNode = self.findMin(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right,minNode.val)
        return root
        