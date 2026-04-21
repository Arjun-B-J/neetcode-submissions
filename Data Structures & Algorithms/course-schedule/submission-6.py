class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def dfs(src,adj,visit,path)->bool:
            if src in path:
                return False
            if src in visit:
                return True
            path.add(src)
            visit.add(src)
            for nei in adj[src]:
                if not dfs(nei,adj,visit,path):
                    return False
            path.remove(src)
            return True

        visit = set()
        path = set()
        adj = {}
        for u,v in prerequisites:
            if u not in adj:
                adj[u]=[]
            if v not in adj:
                adj[v]=[]
            adj[u].append(v)
        
        for src in adj:
            if not dfs(src,adj,visit,path):
                return False
        return True