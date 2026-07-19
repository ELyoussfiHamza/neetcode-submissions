class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quickSort(nums , 0 , len(nums) - 1)

    
    def quickSort(self , arr , l , h):
        
        if l >= h:
            return
        
        index = self.partition(arr , l , h)

        self.quickSort(arr , l , index - 1)
        self.quickSort(arr , index + 1 , h)

    def partition(self , arr:List[int] , l , r):
        pivot = arr[l]

        left , right = l+1 , r

        while left <= right:
            
            while left <= right and arr[left] <= pivot:
                left+=1
            
            while right >= left and arr[right] > pivot:
                right-=1
            
            if left < right:
                arr[left] , arr[right] = arr[right] , arr[left]
            
        
        arr[l] , arr[right] = arr[right] , arr[l]

        return right

        
        
        