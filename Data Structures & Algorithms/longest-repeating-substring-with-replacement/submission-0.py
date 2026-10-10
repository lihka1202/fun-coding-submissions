class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # The basic idea is very simple, simply need to keep track of what is the max number of
        # replacements we can do at any point in time
        L,R = 0, 0
        dct = {}
        res = float("-inf")
        while R < len(s):
            dct[s[R]] = 1 + dct.get(s[R], 0)
            
            while ((R - L + 1) - max(dct.values())) > k:
                # Ie we cannot replace exactly anymore, forced to contract the window
                dct[s[L]] -= 1
                L += 1
            res = max(res, R - L + 1)
            R += 1
        return res