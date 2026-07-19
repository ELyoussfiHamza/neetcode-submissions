class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        mid = len(nums) // 2
        arr = []
        left_sorted = self.sortArray(nums[:mid])
        right_sorted = self.sortArray(nums[mid:])

        i , j = 0 , 0 

        while i < len(left_sorted) and j < len(right_sorted):
            if left_sorted[i] < right_sorted[j]:
                arr.append(left_sorted[i])
                i+=1
            elif left_sorted[i] > right_sorted[j]:
                arr.append(right_sorted[j])
                j+=1
            else:
                arr.extend([left_sorted[i],left_sorted[i]])
                i+=1
                j+=1
        
        while i < len(left_sorted):
            arr.append(left_sorted[i])
            i+=1
        while j < len(right_sorted):
            arr.append(right_sorted[j])
            j+=1
        
        return arr


        