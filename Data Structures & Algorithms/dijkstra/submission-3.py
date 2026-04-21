import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        #initialze adjaceny list
        for i in range(n):
            adj[i]=[]
        
        #add edge and weight
        for edge in edges:
            u,v,w = edge
            adj[u].append((v,w))
        minHeap = []

        heapq.heappush(minHeap,(0,src))
        distance = {}
        while minHeap:
            w1,u = heapq.heappop(minHeap)
            #if already there, greedy approch assumes that it is already the smallest
            if u in distance:
                continue
            distance[u] = w1
            for v,w2 in adj[u]:
                if v not in distance:
                    heapq.heappush(minHeap,(w1+w2,v))
        
        for i in range(n):
            if i not in distance:
                distance[i]=-1
        return distance


