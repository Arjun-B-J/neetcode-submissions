class TreeNode:
    def __init__(self):
        self.word=False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TreeNode()
            cur = cur.children[c]
        cur.word=True

    def search(self, word: str) -> bool:
        def dfs(j,root):
            for i in range(j,len(word)):
                if word[i] =='.':
                    for child in root.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if word[i] not in root.children:
                        return False
                    root = root.children[word[i]]
            return root.word            
        

        return dfs(0,self.root)
