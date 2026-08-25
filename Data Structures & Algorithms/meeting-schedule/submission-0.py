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
        
        start = intervals[0].start
        end = intervals[0].end

        for meet in intervals[1:]:
            if (start<meet.start<end) :
                return False
            
            start = min(start,meet.start)
            end = max(end,meet.end)
        
        return True