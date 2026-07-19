class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for ele in numbers:
            indexx = target-ele 
            try:
                otherIndex = numbers.index(indexx)
    
                return [numbers.index(ele)+1,otherIndex+1]
            except:
                continue
            