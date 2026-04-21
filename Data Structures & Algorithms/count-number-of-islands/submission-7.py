from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visit = set()
        islands = 0
        rL = len(grid)
        cL = len(grid[0])
        def bfs(i,j):
            q = deque()
            q.append((i,j))
            visit.add((i,j))
            while q:
                for k in range(len(q)):
                    r,c = q.popleft()
                    directions = [(0,1),(1,0),(0,-1),(-1,0)]
                    for dr,dc in directions:
                        nR = r+dr
                        nC = c+dc
                        if min(nR,nC)<0 or nR == rL or nC == cL or ((nR,nC) in visit) or grid[nR][nC]=="0":
                            continue
                        else:
                            visit.add((nR,nC))
                            q.append((nR,nC))

        for i in range(rL):
            for j in range(cL):
                if (i,j) not in visit and grid[i][j]!="0":  
                    bfs(i,j)
                    islands+=1
        return islands