# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, left_sub, right_sub):
        if not left_sub and not right_sub:
            return True

        if not left_sub or not right_sub:
            return False
        
        if left_sub.val != right_sub.val:
            return False

        return self.dfs(left_sub.right, right_sub.left) and self.dfs(left_sub.left, right_sub.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # base case
        # if the root is none
        #   return true
        # if one of the children is none
        #   return false
        if not root or (not root.left and not root.right):
            return True

        return self.dfs(root.left, root.right)