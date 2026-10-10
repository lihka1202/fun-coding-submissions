class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMax = -float("inf")
        res = []
        for i in range(len(prices)-1, -1, -1):
            currMax = max(prices[i], currMax)
            res.append(currMax)
        maxProfit = -float("inf")
        res = res[::-1]
        for i in range(len(prices)):
            maxProfit = max(maxProfit, res[i] - prices[i])
        return maxProfit