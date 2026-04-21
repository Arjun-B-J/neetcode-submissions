class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        print(intervals)
        ans = 0
        cur = intervals[0]
        for i in range(1,len(intervals)):
            if not (intervals[i][0]>=cur[1] or intervals[i][1]<=cur[0]):
                ans+=1
            else:
                cur = intervals[i]

        return ans