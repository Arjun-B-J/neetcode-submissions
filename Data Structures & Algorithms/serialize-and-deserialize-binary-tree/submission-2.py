# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = [] #will make it as string at last
        def dfs(root):#will do preorder traversal
            if not root:
                res.append("N")
                return
            res.append(str(root.val)) #we make it as str
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        res = data.split(",")
        i = 0
        def dfs():#we do preorder to get back the tree
            nonlocal i
            if res[i] == "N":
                i+=1 #move i in this case N is null and we need to fetch the next in case if any not completed by preorder
                return None
            root = TreeNode(int(res[i]))
            i+=1 #we took a val here we need to fetch the next
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()
