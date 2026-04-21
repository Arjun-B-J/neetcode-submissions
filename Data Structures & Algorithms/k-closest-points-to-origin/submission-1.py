class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance =[]
        for point in points:
            distance.append([[(point[0]**2 + point[1]**2)**0.5],point])
        kSmallest = heapq.nsmallest(k,distance)
        ans = []
        for ele in kSmallest:
            ans.append(ele[1])
        return ans
    
        