import heapq
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i]=[]
        #Undirected, DONT FORGET TO ADD BOTH    
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        
        minHeap = []
        visit = set()
        #initialize with vertex 0
        visit.add(0)
        for v,w in adj[0]:
            heapq.heappush(minHeap,(w,0,v))
        mst = []
        cost = 0
        while minHeap:
            w,u,v = heapq.heappop(minHeap)
            if v in visit:
                continue
            mst.append((u,v,w))
            cost+=w
            visit.add(v)

            for v2,w2 in adj[v]:
                if v2 not in visit:
                    heapq.heappush(minHeap,(w2,v,v2)) #we need to optimize the total greedily
        
        if len(mst)!=n-1:
            return -1
        return cost