"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
        print(start)
        print(end)
        i,j,gc,res = 0,0,0,0
        while i < len(start):
            if start[i] < end[j]:
                i += 1
                gc += 1
            else:
                j += 1
                gc -= 1
            res = max(res, gc)
        return res