class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o','u'}
        ans = []
        vowled = [int(word[0] in vowels and word[-1] in vowels) for word in words]
        for l , r in queries:
            ans.append(sum(vowled[l:r+1]))
        

        return ans