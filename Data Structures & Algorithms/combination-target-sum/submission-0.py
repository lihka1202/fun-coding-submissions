class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        def dfs(i, comb, sum):
            if i >= len(candidates):
                return 
            if sum > target:
                return
            if sum == target:
                res.append(comb.copy())
                return
            
            # use the current number
            comb.append(candidates[i])
            dfs(i, comb, sum + candidates[i])

            # Skip this number
            comb.pop()
            dfs(i + 1, comb, sum)
        dfs(0, comb, 0)
        return res