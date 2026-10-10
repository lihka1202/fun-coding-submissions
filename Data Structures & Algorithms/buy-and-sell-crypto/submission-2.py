class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # stk = [prices[-1]]
        rngMax = prices[-1]
        res = -float("inf")
        for i in range(len(prices)-2, -1, -1):
            rngMax = max(rngMax, prices[i])
            res = max(res, rngMax - prices[i])
        return res if res != -float("inf") else 0