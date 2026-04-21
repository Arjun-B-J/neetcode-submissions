import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heap.append(stone*-1)
        heapq.heapify(heap)
        while heap:
            if len(heap)==1:
                return heap[0]*-1
            f,s = heapq.heappop(heap)*-1,heapq.heappop(heap)*-1
            net = f-s if f>s else s-f
            if net!=0:
                heapq.heappush(heap,net*-1)

        return 0
        