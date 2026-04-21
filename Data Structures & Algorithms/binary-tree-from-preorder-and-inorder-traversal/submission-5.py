class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)} #Of inorder
        def dfs(preorder,inorder):
            if not preorder or not inorder:
                return None

            root = TreeNode(preorder[0])
            mid = indices[preorder[0]]
            root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
            root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
            return root
        return dfs(preorder,inorder)
        