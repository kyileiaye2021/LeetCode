# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, targetSum):
        if not root:
            return False

        targetSum = targetSum - root.val

        if not root.left and not root.right and targetSum == 0: # at the leaf node the sum val should be 0
            return True

        left_subtree = self.dfs(root.left, targetSum)
        right_subtree = self.dfs(root.right, targetSum)

        return left_subtree or right_subtree


    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # input: 1
        #       / \
        #      3   5
        #     /
        #    5
        # target = 4
        # output: false

        # input: 1
        # target = 1
        # output: true

        # input: 1
        # target = 5
        # output: false

        # dfs
        # preorder traversal
        # base case
        # if curr node is none --> return 
        # check if the curr node is leaf
        #   check if the sum is equal to the target val
        #       return True
        # update sum (curr val + call left subtree )
        # update sum (curr val + call right subtree )
        # 
        return self.dfs(root, targetSum)