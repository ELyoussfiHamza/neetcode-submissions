class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        n = len(nums)
        hm = {}
        size = 0
        for e in nums:
            depth = 0
            v = e -1
            while v in hm:
                v-=1
                depth+=1
            v = e+1
            while v in hm:
                v+=1
                depth+=1
            size = max (size ,depth+1)
            if e not in hm:
                hm[e] = 1
        return size
                