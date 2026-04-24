# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float('-inf')
        def dfs(root):
            nonlocal max_path_sum
            if not root:
                return 0

            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)

            # cur_path_sum = max(root.val, root.val + left, root.val + right, root.val + left + right)
            cur_path_sum = left + right + root.val 
            max_path_sum = max(max_path_sum, cur_path_sum)

            return root.val + max(left , right)

        dfs(root)
        return max_path_sum
