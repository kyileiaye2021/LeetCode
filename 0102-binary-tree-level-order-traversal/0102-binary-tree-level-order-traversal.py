# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs
        # queue
        # add the root to the queue
        # res list
        # until queue is empty
        #   pop out the queue
        #   append it to the res
        #   go to its children
        #       if they are not none, add them to the queue

        # return res

        queue = deque()
        queue.append(root)
        res = []

        if not root:
            return res

        while queue:

            length = len(queue)
            cur_res = []

            for i in range(length):

                cur_node = queue.popleft()
                cur_res.append(cur_node.val)

            res.append(cur_res)

            if cur_node.left:
                queue.append(cur_node.left)

            if cur_node.right:
                queue.append(cur_node.right)

        return res