from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        rl,cl = len(grid),len(grid[0])
        length = 0
        
        q = deque()
        visit = set()
        if grid[0][0]!=0:
            return -1
        q.append((0,0))
        visit.add((0,0))
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                if r == rl-1 and c == cl-1:
                    return length+1
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if min(nr,nc)<0 or nr==rl or nc==cl or (nr,nc) in visit or grid[nr][nc]==1:
                        continue
                    else:
                        visit.add((nr,nc))
                        q.append((nr,nc))
            length+=1
        return -1

        