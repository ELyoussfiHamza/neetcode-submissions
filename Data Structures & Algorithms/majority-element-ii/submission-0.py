class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        bar = int(n/3)
        freq = Counter(nums)

        return [ e for e , f in freq.items() if f > bar]
