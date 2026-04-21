class TrieNode:
    def __init__(self):
        self.children = {}  # Maps character -> TrieNode for each child
        self.word = False   # True if this node marks the end of a valid word


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()  # Empty root node; doesn't represent any character

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            # Create a new node for the character if it doesn't already exist
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        # Mark the final node as the end of a complete word
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j,root):
            cur = root
            for i in range(j,len(word)):
                if word[i]=='.':
                    for child in cur.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if word[i] not in cur.children:
                        return False
                    cur=cur.children[word[i]]
            return cur.word


        return dfs(0,self.root)