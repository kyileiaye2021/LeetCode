# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, balanced):
        if not root:
            return 0

        left_subtree = self.dfs(root.left, balanced)
        right_subtree = self.dfs(root.right, balanced)

        if abs(left_subtree - right_subtree) > 1:
            balanced[0] = False
        return (1 + max(left_subtree, right_subtree))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # base case 
        # if the curr root is none, return 0

        # 1 + go to the left subtree
        # 1 + go to right subtree

        # check if the diff between the curr left and curr right is > 1
        #   return False

        # return left subtree and right subtree
        balanced = [True]
        self.dfs(root, balanced)
        return balanced[0]