# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, res):
        if not root:
            return 0
        left = self.dfs(root.left, res)
        right = self.dfs(root.right, res)

        left = max(0, left)
        right = max(0, right)

        res[0] = max(res[0], (left + right + root.val))
        return root.val + max(left, right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        self.dfs(root, res)
        return res[0]
        