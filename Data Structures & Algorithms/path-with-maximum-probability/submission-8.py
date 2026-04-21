class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {}
        for i in range(n):
            adj[i]= []
        #Undirected Graph
        for i in range(len(edges)):
            adj[edges[i][0]].append((edges[i][1],succProb[i]))
            adj[edges[i][1]].append((edges[i][0],succProb[i]))
      
        maxHeap = []
        distance = {}
        #prob was 1 initially 
        heapq.heappush(maxHeap,(1,start_node))

        while maxHeap:
            w1,u = heapq.heappop(maxHeap)
            w1=abs(w1)
            if u == end_node:
                return w1
            if u in distance:
                continue
            distance[u] = w1
            for v,w2 in adj[u]:
                if v not in distance:
                    heapq.heappush(maxHeap,(-w1*w2,v))
            
        return 0