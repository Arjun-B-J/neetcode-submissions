# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        visited = [False]
        cur = root
        ans = []
        while stack:
            cur,visit = stack.pop(),visited.pop()
            if cur:
                if visit:
                    ans.append(cur.val)
                else:
                    stack.append(cur)
                    visited.append(True)
                    stack.append(cur.right)
                    visited.append(False)
                    stack.append(cur.left)
                    visited.append(False)
        return ans

        