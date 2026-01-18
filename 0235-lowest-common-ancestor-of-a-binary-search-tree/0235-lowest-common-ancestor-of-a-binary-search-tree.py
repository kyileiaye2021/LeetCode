# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # dfs
        # if not root
        # return none
        # if curr root between p and q inclusively
        #   return the node
        # if the curr root is less than both p and q,
        #   go to right subtree
        # if curr root > p andq
        #   go to left subtree

        def dfs(root):
            if not root:
                return None

            if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
                return root

            elif root.val < p.val and root.val < q.val:
                return dfs(root.right)

            else:
                return dfs(root.left)

        return dfs(root)

        