class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        s = {}
        for i in range(n):
            if target - nums[i] in s:
                return [min(s[target - nums[i]] , i),max(s[target - nums[i]] , i)]
            s[nums[i]] = i
        return []
