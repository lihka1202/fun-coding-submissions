# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxCount = 0

        def countNodes(root, currMax):
            nonlocal maxCount
            if not root:
                return
            if root.val >= currMax:
                maxCount += 1
                currMax = root.val
            countNodes(root.left, currMax)
            countNodes(root.right, currMax)
        
        countNodes(root, -101)
        return maxCount