#classic Dijkstra's 
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minHeap = []
        adj = {}
        for i in range(1,n+1):
            adj[i]=[]
        for time in times:
            u,v,t = time
            adj[u].append((v,t))

        heapq.heappush(minHeap,(0,k))
        bestTime = {}
        while minHeap:
            t1,u = heapq.heappop(minHeap)
            if u in bestTime:
                continue
            bestTime[u]=t1

            for v,t2 in adj[u]:
                if v not in bestTime:
                    heapq.heappush(minHeap,((t2+t1),v))
        minTime = -1
        for i in range(1,n+1):
            if i not in bestTime:
                return -1
            minTime = max(minTime,bestTime[i])
        return minTime
        
            