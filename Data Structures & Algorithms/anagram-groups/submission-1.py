class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        hm = {}

        for e in strs:
            
            sor = "".join(sorted(e))
  
            if sor not in hm:
                hm[sor] = []
            hm[sor].append(e)
        
        return [v for v in hm.values()]
