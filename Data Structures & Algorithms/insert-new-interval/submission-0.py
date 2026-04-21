class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i,interval in enumerate(intervals):
            print(interval)
            if newInterval[1]<interval[0]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            
            elif newInterval[0]>interval[1]:
                res.append(interval)
            else:
                newInterval = [min(newInterval[0],interval[0]),max(newInterval[1],interval[1])]
        res.append(newInterval)
        return res