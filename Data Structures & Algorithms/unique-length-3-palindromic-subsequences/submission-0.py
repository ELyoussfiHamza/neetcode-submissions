class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        picked = set()
        ans : int = 0
        for i , e in enumerate(s):
            if e not in picked:
                picked.add(e)
                last_occ = s.rfind(e)
                if last_occ - i <= 1:
                    continue
                
                middle_pool = set(s[i+1:last_occ])
                ans += len(middle_pool)
        return ans




