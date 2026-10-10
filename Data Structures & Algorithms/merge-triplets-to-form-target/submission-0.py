class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # The greedy idea is to keep choosing the max and at some point it will lead to the result
        # if not gg
        # or if you randomly reach there
        maxi,maxj,maxk = 0,0,0
        for tp in triplets:
            if tp[0] <= target[0] and tp[1] <= target[1] and tp[2] <= target[2]:
                maxi = max(maxi, tp[0])
                maxj = max(maxj, tp[1])
                maxk = max(maxk, tp[2])
            # If you reach the ans
            if (target[0] == maxi and target[1] == maxj and target[2] == maxk):
                return True
        return False


# class Solution:
#     def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
#         #triplets.sort()
#         a,b,c = 0,0,0
#         for i in range(len(triplets)):
#             if(triplets[i][0]<=target[0] and triplets[i][1]<=target[1] and triplets[i][2]<=target[2]):
#                 a = max(a,triplets[i][0])
#                 b = max(b,triplets[i][1])
#                 c = max(c,triplets[i][2])
#             if a==target[0] and b==target[1] and c==target[2]:
#                 return True
#         return False