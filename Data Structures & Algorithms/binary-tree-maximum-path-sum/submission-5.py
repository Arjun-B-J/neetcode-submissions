# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val #max path sum with split
        def dfs(root): #we return without split path sum
            if not root:
                return 0
            maxLeftSum = max(dfs(root.left),0) #without split
            maxRightSum = max(dfs(root.right),0) #without split
            
            nonlocal res
            res = max(res,root.val+maxLeftSum+maxRightSum) #try split and update res
            return root.val + max(maxLeftSum,maxRightSum) #return max path sum without split
        dfs(root)
        return res

        