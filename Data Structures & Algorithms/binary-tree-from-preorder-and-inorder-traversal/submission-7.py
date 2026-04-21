class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. Map construction O(N) - Done only once
        indices = {val: idx for idx, val in enumerate(inorder)}
        
        # Use a mutable reference for the preorder index (or a class variable)
        self.pre_idx = 0 

        def dfs(in_left, in_right):
            # Base case: if no elements left in the current inorder slice
            if in_left > in_right:
                return None
            
            # 2. Get the current root value from preorder
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1 # Move to next element in preorder

            # 3. Split inorder using the map (O(1) lookup)
            mid = indices[root_val]

            # 4. Recurse using indices - No slicing!
            root.left = dfs(in_left, mid - 1)
            root.right = dfs(mid + 1, in_right)
            
            return root

        return dfs(0, len(inorder) - 1)