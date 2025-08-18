# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, k, n, output):
        if not root:
            return 

        # left subtree
        self.dfs(root.left, k, n, output)

        # current
        n[0] += 1
        if n[0] == k:
            output[0] = root.val

        # right subtree
        self.dfs(root.right, k, n, output)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # dfs
        # root = 5
        #       / \
        #      3   6
        #     / \
        #    2.  4
        #   /
        #  1
        # output: 3

        # root = 5, k = 1
        # output = 5

        # input: 3, k = 1
        #       / \
        #      1.  4
        #       \
        #        2
        # output: 1

        # input: 3, k = 2
        #       / \
        #      1.  4
        #       \
        #        2
        # output: 2

        # helper func (root, k, n) n = 0
        # inorder traversal (dfs)
        # base case
        # if the root becomes none, return 

         # recursive case
        # call left subtree
        # in each recursive call, increment n check if n == k:
        #   store the root.val
        # call right subtree
        n = [0]
        output = [0]
        self.dfs(root, k, n, output)
        return output[0]




