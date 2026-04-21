class TrieNode:
    def __init__(self):
        self.children = {}  # Maps character -> TrieNode
        self.word = False   # True if this node marks the end of a valid word

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])

        # Build a trie from all target words so we can check
        # multiple words simultaneously during a single DFS path
        root = TrieNode()
        for word in words:
            root.addWord(word)

        visit = set()   # Tracks cells used in the current DFS path (avoid reuse)
        result = set()  # Use a set to avoid duplicate words

        def dfs(r, c, node, word):
            # Prune if: out of bounds, cell not in trie branch, or already visited
            if (min(r, c) < 0 or r == ROWS or c == COLS
                    or board[r][c] not in node.children
                    or (r, c) in visit):
                return

            visit.add((r, c))           # Mark cell as part of current path
            word += board[r][c]         # Extend current word with this character
            node = node.children[board[r][c]]  # Descend into trie

            if node.word:
                result.add(word)        # Found a complete word — record it

            # Explore all 4 directions
            dfs(r + 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c - 1, node, word)

            visit.remove((r, c))        # Backtrack — unmark cell for other paths

        # Try starting a DFS from every cell on the board
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, root, "")

        return list(result)