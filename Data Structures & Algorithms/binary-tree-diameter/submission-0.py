# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # When you see each root, go left and right
        if not root:
            return 0
        
        def getHeight(node):
            if not node:
                return 0
            return 1 + max(getHeight(node.left), getHeight(node.right))
        
        res = getHeight(root.left) + getHeight(root.right)
        return max(max(res, self.diameterOfBinaryTree(root.left)), self.diameterOfBinaryTree(root.right))
        
        # def getMax(node):
        #     if not node:
        #         return 0
        #     res = getHeight(node.left) + getHeight(node.right)
        #     return max(max(res, getMax(node.left)), getMax(node.right))