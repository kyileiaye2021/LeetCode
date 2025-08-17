# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # edge cases
        # input: 6, p = 6, q = 6
        # output - 6

        # inputs: 6, p = 6, q = 7
        #           \
        #            7
        # output: 6

        # base case
        # if p or q is root node, return root node
        # if p and q are less than the root node
        #   go to left subtree
        # if p and q are greater than the root node
        #   go to the right subtree
        if p.val == root.val or q.val == root.val or (p.val > root.val and q.val < root.val) or (p.val < root.val and q.val > root.val) :
            return root

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

