# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:

        # base case
        # return true when root == None

        # recursive case
        # if curr.left val != curr.right val
        #   return false

        # call left sub tree and right sub tree
        # return true if both left and right return true

        def recur_symmetric(left_node, right_node):
            if not left_node and not right_node:
                return True

            if not left_node:
                return False

            if not right_node:
                return False

            if left_node.val != right_node.val:
                return False

            return recur_symmetric(left_node.left, right_node.right) and recur_symmetric(left_node.right, right_node.left)
        return recur_symmetric(root.left, root.right)


        