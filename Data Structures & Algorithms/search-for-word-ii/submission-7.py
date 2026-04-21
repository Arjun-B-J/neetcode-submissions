class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    def addWord(self,word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS,COLS = len(board),len(board[0])
        root = TrieNode()
        for word in words:
            root.addWord(word)
        visit,result = set(),set()
        def dfs(r,c,node,word):
            if min(r,c)<0 or r==ROWS or c==COLS or board[r][c] not in node.children or (r,c) in visit:
                return False

            visit.add((r,c))
            word+=board[r][c]
            node = node.children[board[r][c]]
            if node.word:
                result.add(word)
            dfs(r+1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c-1,node,word)

            visit.remove((r,c))

        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j,root,"")
        return list(result)
