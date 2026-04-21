# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #idea is to find the lowest common ancestor , that is depth fartest away from root, so have to find the split point
        cur = root
        while True:
            if not cur:
                return None
            if p.val > cur.val and q.val > cur.val: #both are in the right subtree
                cur=cur.right
                continue
            if p.val < cur.val and q.val < cur.val: #both are in the left subtree
                cur=cur.left
                continue
            return cur
        
            