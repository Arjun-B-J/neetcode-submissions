import heapq
class MedianFinder:

    def __init__(self):
        self.small = [] #Max Heap
        self.large = [] #Min Heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,num*-1)
        #check heap min max property is maintained
        if self.small and self.large and self.small[0]*-1 > self.large[0]:
            heapq.heappush(self.large,heapq.heappop(self.small)*-1)
        
        #check if length is skwed
        if len(self.small) - len(self.large) > 1:
            heapq.heappush(self.large,heapq.heappop(self.small)*-1)  
        elif len(self.large) - len(self.small) > 1:
            heapq.heappush(self.small,heapq.heappop(self.large)*-1)

    def findMedian(self) -> float:
        if len(self.small)>len(self.large):
            return self.small[0]*-1
        elif len(self.large)>len(self.small):
            return self.large[0]
        else:
            return (self.small[0]*-1 + self.large[0])/2


        
        