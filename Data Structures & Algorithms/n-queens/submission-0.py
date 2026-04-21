class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range(n)]
        cols = set()
        positiveDiagonal = set() # r+c is constant
        negativeDiagonal = set() #r-c is constant
        res = []

        def backtrack(r):
            if r==n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in cols or r+c in positiveDiagonal or r-c in negativeDiagonal:
                    continue
                board[r][c] = 'Q'
                cols.add(c)
                positiveDiagonal.add(r+c)
                negativeDiagonal.add(r-c)

                backtrack(r+1)

                board[r][c] = '.'
                cols.remove(c)
                positiveDiagonal.remove(r+c)
                negativeDiagonal.remove(r-c)

        backtrack(0)
        return res

            