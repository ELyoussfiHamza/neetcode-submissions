class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        s2 = set(arr2)
        s1 = set(arr1)
        h = Counter(arr1)

        last = sorted([e for e in arr1 if e not in s2])
        
        first = []
        for e in arr2:
            
            if e not in s1:
                continue
            first.extend([e] * h[e])
            s1.remove(e)
        
        return first + last
        