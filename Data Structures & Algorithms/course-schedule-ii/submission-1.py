class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(src,adj,path,visit) -> bool:
            if src in path:
                return False
            if src in visit:
                return True
            path.add(src)
            visit.add(src)
            
            for nei in adj[src]:
                if not dfs(nei,adj,path,visit):
                    return False
            path.remove(src)
            topSort.append(src)
            return True
            
        path = set()
        visit = set()
        adj = {}
        for i in range(numCourses):
            adj[i]=[]
        for u,v in prerequisites:
            adj[u].append(v)
        topSort = []
        for src in adj:
            if not dfs(src,adj,path,visit):
                return []
        return topSort