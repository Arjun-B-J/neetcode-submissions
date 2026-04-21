class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #reverse thinking needed
        #capture everything except the unsurrounded region
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        visit = set()
        ROW,COL = len(board),len(board[0])

        def dfs(r,c):
            if min(r,c)<0 or r==ROW or c==COL or (r,c) in visit or board[r][c]=='X':
                return
            visit.add((r,c))
            board[r][c]='T'
            for dr,dc in directions:
                dfs(r+dr,c+dc)
        
        for i in range(ROW):
            dfs(i,0)
            dfs(i,COL-1)
        for i in range(COL):
            dfs(0,i)
            dfs(ROW-1,i)

        for i in range(ROW):
            for j in range(COL):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='T':
                    board[i][j]='O'

            