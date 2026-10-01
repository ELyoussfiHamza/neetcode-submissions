class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n  = len(arr)
        ans = 0
        pref = [0] * n
        pref [ 0 ] = arr[0]
        for i in range(1,n):
            pref[i] = arr[i] + pref[i-1]
        hm = {0 : 1, 1 : 0}
        for j in range(n):
            if pref[j] % 2 == 0:
                hm[0] +=1
                ans = (hm[1] + ans) % MOD
            else:
                hm[1] +=1 
                ans = (hm[0] + ans ) % MOD

        
        return ans





