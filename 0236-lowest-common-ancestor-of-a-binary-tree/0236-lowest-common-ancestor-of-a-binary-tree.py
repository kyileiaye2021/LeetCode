# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base case
        # if root == none
        # return none
        # recursive step
        # left = recur func on left subtree
        # right = recur func on right subtree
        # if not left 
        #   return right
        # elif not right:
        #   return left
        # else:
        #   return root

        def recur_LCA(root, p, q):
            # base case
            if not root:
                return None

            if root.val == p.val or root.val == q.val:
                return root

            left = recur_LCA(root.left, p, q)
            right = recur_LCA(root.right, p, q)

            if not left:
                return right
            elif not right:
                return left
            else:
                return root
        return recur_LCA(root, p, q)