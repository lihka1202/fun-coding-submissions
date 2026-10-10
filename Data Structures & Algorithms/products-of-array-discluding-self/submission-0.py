class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        res = []
        prod = 1
        for n in nums:
            prod *= n
            left.append(prod)
        prod = 1
        for n in nums[::-1]:
            prod *= n
            right.append(prod)
        print("left: ",left)
        right = right[::-1]
        print("right: ",right)
        for i in range(len(nums)):
            if i == 0:
                res.append(right[i+1])
            elif i == len(nums)-1:
                res.append(left[i-1])
            else:
                res.append(left[i-1] * right[i+1])
        return res