class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {} 
        for s in strs:
            orig = s
            s = str(sorted(s))
            if s not in dct:
                dct[s] = []
            dct[s].append(orig)
        res = dct.values()
        return res
            