"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key= lambda x:x.start)
        prev = intervals[0]
        for interval in intervals[1:]:
            if not (prev.start>=interval.end or prev.end<=interval.start):
                return False
            else:
                prev= interval
        return True
