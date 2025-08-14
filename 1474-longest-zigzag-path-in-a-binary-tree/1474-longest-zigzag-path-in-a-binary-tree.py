# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, left, step, max_len):
        if not root:
            return

        max_len[0] = max(step, max_len[0])
        if left: # parent coming from left
            self.dfs(root.right, False, step + 1, max_len) # go to the right, increment the step 
            self.dfs(root.left, True, 1, max_len) # go to the left, reset to 1

        else: # parent coming from the right
            self.dfs(root.left, True, step + 1, max_len) # go to the left, increment the step
            self.dfs(root.right, False, 1, max_len) # go to the right, reset to 1

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # input: 1
        # output: 0

        # input: 1
        #       /
        #      1
        #     /
        #    1
        # output: 1

        # input: 1
        #       /
        #      1
        # output: 1

        # input: 1
        #       / \
        #      2   2
        #       \
        #        3
        # output: 2

        # dfs
        # preorder traversal

        max_len = [0]
        self.dfs(root.left, True, 1, max_len)
        self.dfs(root.right, False, 1, max_len)
        return max_len[0]


