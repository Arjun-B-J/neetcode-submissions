class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(src,visit,path,adj)->bool:
            if src in path:
                return False
            if src in visit:
                return True
            visit.add(src)
            path.add(src)
            for nei in adj[src]:
                if not dfs(nei,visit,path,adj): #Handle Cycles here
                    return False
            topSort.append(src)
            path.remove(src) #remvove from current explored path
            return True
        
        #Build Adjacency List
        adj = {}
        for i in range(n):
            adj[i]=[]
        for u,v in edges:
            adj[u].append(v)
        #Track All Visited
        visit = set()
        path = set() #Track the current Path explored in case of cycle
        topSort = []
        for i in range(n):
            if not dfs(i,visit,path,adj):
                return []
        topSort.reverse()
        return topSort

        