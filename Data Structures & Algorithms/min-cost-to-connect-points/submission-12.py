#classic Prims
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def calcDistance(p1,p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        def returnTupleFromPoint(point):
            return (point[0],point[1])
        adj = {}
        for point in points:
            adj[returnTupleFromPoint(point)]=[]
        #Undirected, DONT FORGET TO ADD BOTH 
        for point in points:
            for i in range(len(points)):
                if points[i]==point:
                    continue
                adj[returnTupleFromPoint(point)].append((points[i],calcDistance(point,points[i])))

        minHeap = []
        for v,w in adj[returnTupleFromPoint(points[0])]:
            heapq.heappush(minHeap,(w,points[0],v))

        visit = set()
        visit.add(returnTupleFromPoint(points[0]))
        mst = []
        cost = 0
        while minHeap:
            w,u,v = heapq.heappop(minHeap)
            if returnTupleFromPoint(v) in visit:
                continue
            mst.append((u,v,w))
            cost+=w
            visit.add(returnTupleFromPoint(v))

            for v2,w2 in adj[returnTupleFromPoint(v)]:
                if returnTupleFromPoint(v2) not in visit:
                    heapq.heappush(minHeap,(w2,v,v2)) #we need to optimize the total greedily
        n = len(points)
        if len(mst)!=n-1:
            return -1
        return cost