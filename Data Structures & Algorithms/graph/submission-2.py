from collections import deque
class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = []
        if dst not in self.graph:
            self.graph[dst] = []
        if dst not in self.graph[src]:
            self.graph[src].append(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.graph and dst in self.graph[src]:
            self.graph[src].remove(dst)
            return True
        return False

    def bfs(self, src:int, dst:int) -> bool:
        q = deque()
        visit = set()
        q.append(src)
        visit.add(src)

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == dst:
                    return True
                for edges in self.graph[cur]:
                    if edges not in visit:
                        visit.add(edges)
                        q.append(edges)
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        return self.bfs(src,dst)

