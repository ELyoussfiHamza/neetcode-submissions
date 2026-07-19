class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans = ""
        h = Counter(s)
        for c in order:
            if c in s:
                ans+=c * h[c]
        
        
        for c in s:
            if c not in order:
                ans+=c
        return ans