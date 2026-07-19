class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        events = []
        res = []
        for s , e in intervals:
            events.append((s, - 1))
            events.append((e , 1))
        
        events.sort(key = lambda x : (x[0] , x[1]))
        curr = 0
        start = None
        for t , s in events:
            if start is None:
                start = t
                curr+=s
                continue
            curr+=s

            if curr == 0:
                res.append([start , t])
                start = None
        return res