class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [e[0] for e in sorted(zip(names , heights) , key = lambda x : -x[1])]

