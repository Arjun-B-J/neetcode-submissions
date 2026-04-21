class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfits = []
        minCapital = [(c,-p) for c, p in zip(capital,profits) ]
        heapq.heapify(minCapital)

        for i in range(k):
            #populate feasible capital ones at the current w val
            while minCapital and minCapital[0][0]<=w:
                c,p = heapq.heappop(minCapital)
                heapq.heappush(maxProfits,p)
            #if none break
            if not maxProfits:
                break
            w+= (-heapq.heappop(maxProfits))
        return w