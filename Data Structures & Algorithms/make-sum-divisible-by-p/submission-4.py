class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        pref_sum = [0]*n
        pref_sum[0] = nums[0]

        for i in range(1,n):
            pref_sum[i] = nums[i] + pref_sum[i-1]
        r = pref_sum[-1] % p
        if  r == 0:
            return 0
        hm = {0:-1}
        res = n
        for i , e in enumerate(pref_sum):
            curr_rem = e % p
            target = (curr_rem - r + p )%p
            if target in hm:
                l = i - hm[target]
                res = min(l , res)
            hm[curr_rem] = i

        return -1 if res == n else res