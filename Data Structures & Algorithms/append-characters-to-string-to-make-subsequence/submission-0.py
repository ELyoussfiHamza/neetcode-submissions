class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        idx = 0
        for i in range(len(s)):
            if idx >= len(t):
                return 0
            
            if t[idx] == s[i]:
                idx+=1
        
        return len(t) - idx
            