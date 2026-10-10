class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dct = {}
        for i,n in enumerate(s):
            dct[n] = i
        print(dct)

        maxR = 0
        currLen = 0
        res = []
        for i,n in enumerate(s):
            maxR = max(dct[n], maxR)
            currLen += 1
            if i == maxR:
                res.append(currLen)
                # reset the current length
                currLen = 0
        return res