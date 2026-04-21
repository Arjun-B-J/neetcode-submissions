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
        def dfs(j, root):
            """
            Recursively search the trie starting from index j in `word`
            and the given trie node.
            """
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    # Wildcard: try every possible child and recurse
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False  # No child branch led to a match
                else:
                    # Regular character: follow the exact edge or fail
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]

            # Consumed all characters — valid only if we're at a word-end node
            return cur.word

        return dfs(0, self.root)