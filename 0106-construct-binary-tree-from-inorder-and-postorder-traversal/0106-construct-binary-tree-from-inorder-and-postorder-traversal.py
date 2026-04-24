# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        cur_node = TreeNode(postorder[-1])
        print(cur_node)
        mid = inorder.index(postorder[-1])
        print(mid)

        cur_node.left = self.buildTree(inorder[:mid],postorder[:mid])
        cur_node.right = self.buildTree(inorder[mid + 1:], postorder[mid:-1])
        return cur_node

        