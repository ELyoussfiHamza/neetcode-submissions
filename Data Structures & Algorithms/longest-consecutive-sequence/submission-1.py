class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        s = set(nums)
        ans = 0
        i = 0
        while i < n:
            if nums[i] - 1 not in s:
                
                # Start of sequence
                l = 0
                curr = nums[i]
                while curr in s:
                    l+=1
                    curr += 1
                i+=1
                ans = max(ans , l)
            else:
                i+=1
        return ans
