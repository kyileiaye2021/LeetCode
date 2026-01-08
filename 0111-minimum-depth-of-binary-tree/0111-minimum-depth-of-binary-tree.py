# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        # bfs
        # queue

        if not root:
            return 0

        q = deque()
        q.append(root)
        curr_depth = 0

        while q:
            
            curr_len = len(q)
            curr_depth += 1
            for _ in range(curr_len):
                curr_node = q.popleft()

                if not curr_node.left and not curr_node.right:
                    return curr_depth

                if curr_node.left:
                    q.append(curr_node.left)

                if curr_node.right:
                    q.append(curr_node.right)

            