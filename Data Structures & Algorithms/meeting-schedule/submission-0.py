"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x:(x.start, x.end))

        for i in range(len(intervals) - 1):
            print( "(", intervals[i].start, intervals[i].end, ")", "(", intervals[i+1].start, intervals[i+1].end, ")")
            if intervals[i+1].start < intervals[i].end:
                return False
            
        return True