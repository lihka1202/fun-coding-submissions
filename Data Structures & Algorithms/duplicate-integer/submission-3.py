class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         map = {}
         for i in nums:
            if map.get(i)==None:
                map[i]=1
            else:
                return True
         return False