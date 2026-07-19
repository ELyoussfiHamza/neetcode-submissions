class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        l,r = 0 , 0
        ans = 0
        while r < n:

            hm = {}
            while r < n and s[r] not in hm:
                hm[s[r]] = r
                r+=1
            ans = max ( ans , r - l)
            
            if r < n:
                l = hm[s[r]]+1
                r = l

        # ans = max ()
        return ans
