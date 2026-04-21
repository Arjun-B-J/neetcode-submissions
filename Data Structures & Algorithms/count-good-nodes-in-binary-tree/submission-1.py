# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cur =None
        goodNodes = 0
        stack = [(root,root.val)]
        mono = []
        while stack:
            cur,pathMax = stack.pop()
            if cur.val>=pathMax:
                goodNodes+=1
                pathMax=cur.val
            if cur.left:
                stack.append((cur.left,pathMax))
            if cur.right:
                stack.append((cur.right,pathMax))       

        return goodNodes
        