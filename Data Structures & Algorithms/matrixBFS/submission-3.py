from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        visit = set()
        q = deque()
        q.append((0,0))
        rowL=len(grid)
        colL=len(grid[0])
        length = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                if r == rowL-1 and c == colL-1:
                    return length
                directions = [(1,0),(0,1),(0,-1),(-1,0)]
                for dr,dc in directions:
                    newR = r + dr
                    newC = c + dc
                    if min(newR,newC)<0 or newR == rowL or newC == colL or ((newR,newC) in visit) or grid[newR][newC] == 1:
                        continue
                    else:
                        visit.add((newR,newC))
                        q.append((newR,newC))
            length+=1
        return -1
        