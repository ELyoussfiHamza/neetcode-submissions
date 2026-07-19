class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
       
        if len(s) == 0:
            return True
        
        if len(t) == 0:
            return False
        
        idx = 0
        for i in range(len(t)):
            if idx == len(s):
                return True
            if t[i] == s[idx]:
                idx+=1

        return idx == len(s)  