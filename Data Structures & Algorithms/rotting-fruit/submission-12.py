from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        rl,cl = len(grid),len(grid[0])
        time,fresh = 0,0
        q = deque()
        for i in range(rl):
            for j in range(cl):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j))

        while q and fresh>0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr = dr+r
                    nc = dc+c
                    if min(nr,nc)<0 or nr==rl or nc==cl or grid[nr][nc]!=1:
                        continue
                    fresh-=1
                    grid[nr][nc] = 2
                    q.append((nr,nc))
            time+=1
              
     
        return time if fresh==0 else -1
        