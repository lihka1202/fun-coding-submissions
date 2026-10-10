class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dct = {}
        t_dct = {}
        for c in s:
            s_dct[c] = 1 + s_dct.get(c,0)
        for c in t:
            t_dct[c] = 1 + t_dct.get(c,0)
        return s_dct == t_dct