# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # dfs 
        # p,q
        # if p is none but q is not or vice versa
        #   return false
        # check if the curr root is not the same
        #   return false
        # go to left 
        # go to right
        # combine left and right

        def dfs(root1, root2):
            if (root1 and not root2) or (not root1 and root2):
                return False

            if not root1 and not root2:
                return True

            if root1.val != root2.val:
                return False

            left = dfs(root1.left, root2.left)
            right = dfs(root1.right, root2.right)
            return left and right
        
        return dfs(p, q)


            

        