class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # comb = []
        res = []
        def subsets(i, comb):
            if i >= len(nums):
                res.append(comb.copy())
                return 
            # Add
            comb.append(nums[i])
            subsets(i+1, comb)

            # Pop and take the different branch
            comb.pop()
            subsets(i+1, comb)
        subsets(0, [])
        return res