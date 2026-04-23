# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs
        res =[]
        if not root:
            return res
        queue = deque()
        queue.append(root)

        while queue:
            queue_len = len(queue)
            cur_lst = []

            for _ in range(queue_len):
                cur_node = queue.popleft()
                cur_lst.append(cur_node.val)

                if cur_node.left:
                    queue.append(cur_node.left)
                
                if cur_node.right:
                    queue.append(cur_node.right)

            res.append(cur_lst)

        return res

                
        