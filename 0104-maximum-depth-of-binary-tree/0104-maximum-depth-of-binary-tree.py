# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # dfs
        # base case
        # if the root is none: return 0

        # take the max len of (left subtree, right subtree)

        # return 1 + max len

        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))





