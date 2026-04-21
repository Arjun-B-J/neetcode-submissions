class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}
        ROWS,COLS = len(matrix),len(matrix[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(r,c,prevVal):
            if min(r,c)<0 or r==ROWS or c==COLS or prevVal>=matrix[r][c]:
                return 0
            if (r,c) in cache:
                return cache[(r,c)]
            res = 1
            for dr,dc in directions:
                res=max(res,1+dfs(r+dr,c+dc,matrix[r][c]))
            cache[(r,c)] = res
            return cache[(r,c)]
        
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j,-1)
        return max(cache.values())
