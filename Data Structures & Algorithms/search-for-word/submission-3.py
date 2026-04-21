class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()  # Tracks cells used in the current DFS path (avoid reuse)

        def dfs(r, c, i):
            # Successfully matched all characters
            if i == len(word):
                return True

            # Prune if: out of bounds, already visited, or character doesn't match
            if (r >= ROWS or c >= COLS or min(r, c) < 0
                    or (r, c) in path
                    or board[r][c] != word[i]):
                return False

            path.add((r, c))      # Mark cell as part of current path

            # Explore all 4 directions for the next character word[i+1]
            # Short-circuits as soon as any direction finds a complete match
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c - 1, i + 1))

            path.remove((r, c))   # Backtrack — unmark cell for other paths
            return res

        # Try starting a DFS from every cell on the board
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True   # Found a valid path — no need to continue

        return False