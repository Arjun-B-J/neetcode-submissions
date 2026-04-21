import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        heap = []
    
        for num in nums:
            if num not in count:
                count[num]=1
            count[num]+=1
            
        for num in count.keys():
            heapq.heappush(heap,(count[num],num))
            if len(heap)>k:
                heapq.heappop(heap)
        res= []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
            