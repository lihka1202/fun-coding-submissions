class Solution:
    def trap(self, height: List[int]) -> int:
        L,R = 0, len(height) - 1
        maxL, maxR = height[L], height[R]
        res = 0
        while L < R:
            if maxL < maxR:
                # use maxL here
                L += 1
                maxL = max(height[L], maxL)
                res += maxL - height[L]
            else:
                # use maxR here
                R -= 1
                maxR = max(height[R], maxR)
                res += maxR - height[R]
        return res
