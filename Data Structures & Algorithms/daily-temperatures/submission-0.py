class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [30,38,30,36,35,40,28]
        n = len(temperatures)
        res = [0]*n

        st = deque()
        
        for i in range(n-1,-1,-1):
            while len(st) > 0 and  st[-1][0] <= temperatures[i]:
                st.pop()
            
            if len(st) > 0:
                res[i] = st[-1][1] - i
            st.append((temperatures[i],i))
        return res
            
