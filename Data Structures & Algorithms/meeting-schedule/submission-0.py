"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        events = []
        for u in intervals:
            events.append((u.start , 1))
            events.append((u.end,-1))
        
        events.sort(key = lambda x : (x[0] , x[1]))
        curr = 0
        for t , s in events:
            curr += s

            if curr >= 2:
                return False
        return True