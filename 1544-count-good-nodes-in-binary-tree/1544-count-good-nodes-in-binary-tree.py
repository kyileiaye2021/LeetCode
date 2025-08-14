# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root:TreeNode, max_val:int)-> int:
        if not root:
            return 0

        count = 0
        if root.val >= max_val:
            count += 1
            max_val = root.val
        
        left_subtree = self.dfs(root.left, max_val)
        right_subtree = self.dfs(root.right, max_val)
        return count + left_subtree + right_subtree

    def goodNodes(self, root: TreeNode) -> int:
        # dfs
        # preorder traversal
        # base case:
        # if the root node becomes null
        #   return 0
        
        # count = 0
        # check if the curr val is greater than the max val
        #   incrementing the count
        #   max_val = curr val
        # left_subtree = go to left subtree
        # right_subtree = go to right subtree

        # return the count + left + right
        max_val = float('-inf')
        return self.dfs(root, max_val)