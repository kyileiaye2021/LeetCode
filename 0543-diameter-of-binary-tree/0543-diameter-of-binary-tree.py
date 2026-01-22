# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # if there is only one node
        #   output = 0

        # dfs
        # base case
        #   if the root is none
        #       return 0
        # recursive step
        #   left = go to left subtree
        #   right = go to right subtree
        #   diameter = max betwee curr dia and left + right
        #   return 1 + (max between left and right)
        diameter = [0]
        def dfs(root, diameter):
            if not root:
                return 0

            left = dfs(root.left, diameter)
            right = dfs(root.right, diameter)

            diameter[0] = max(diameter[0], left + right)
            return 1 + max(left, right)
        
        dfs(root, diameter)
        return diameter[0]

