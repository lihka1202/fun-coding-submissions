class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        holder = set()

        for n in nums:
            holder.add(n)
        
        return len(holder) != len(nums)
         