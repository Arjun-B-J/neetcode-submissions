class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        cur = intervals[0]
        for i in range(1,len(intervals)):
            if cur[1]<intervals[i][0]: #cur end before the new one
                res.append(cur)
                cur = intervals[i]
            else:
                cur[0],cur[1] = min(cur[0],intervals[i][0]),max(cur[1],intervals[i][1])
        res.append(cur)
        return res

