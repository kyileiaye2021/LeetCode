# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # dfs
        # the node becomes a leaf and target == sum
        #   return true
        # the node becomes none or the node sum value > targetSu
        #   return false
        # go to left subtree
        # go to right subtree
        # return left or right

        def dfs(root, cur_sum):
            if not root:
                return False
            
            cur_sum += root.val 

            if not root.left and not root.right and cur_sum == targetSum:
                return True

            left = dfs(root.left, cur_sum)
            right = dfs(root.right, cur_sum)
            return left or right 

        return dfs(root, 0)
        
        