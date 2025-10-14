# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True

        if not root and subRoot:
            return False

        if root and not subRoot:
            return False

        if root.val != subRoot.val:
            return False
            
        return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        
    def helper(self, root, subRoot):
    
        if not subRoot:
            return True

        if not root:
            return False

        
        if self.sameTree(root, subRoot):
            return True

        return self.helper(root.left, subRoot) or self.helper(root.right, subRoot)
        

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if root is none, subroot is none
        #   return true
        # if root is not none, and subroot is none
        #   return true
        # if root is none, but subroot is not
        #   return false
        # check if the root val is == to subroot val
        #   go to left subtree of both roots
        #   go to right subtree of both roots
        # else
        #   go to left and right subtree of root

        return self.helper(root, subRoot)

