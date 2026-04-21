# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        q1,q2 = deque([p]),deque([q])
        
        while q1 and q2:
            q1Val = q1.popleft()
            q2Val = q2.popleft()
            if not q1Val and not q2Val:
                continue
            if not q1Val and q2Val:
                return False
            if not q2Val and q1Val:
                return False
            if q1Val.val!=q2Val.val:
                return False
            #append children
            q1.append(q1Val.left)
            q1.append(q1Val.right)
        
            q2.append(q2Val.left)
            q2.append(q2Val.right)
        return True