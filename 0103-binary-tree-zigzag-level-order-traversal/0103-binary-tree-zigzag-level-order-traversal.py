# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # bfs

        # queue 
        # add the root node to the queue
        # left = False
        # right = False
        # res = empty

        # while queue is not empty
        #   curr list
        #   for the len of queue
            #   if left is false
            #       popleft the root node
            #       set left to true
            #   else
            #       pop the node and add the vals to the curr list
            #       set left to false
        #   add curr list to the res
        #   if there is left child, add it to the queue
        #   if there is right child, add it to queue

        # return res

        queue = deque()
        queue.append(root)
        left = False
        res = []

        if not root:
            return res

        while queue:
            curr_lst = []
            queue_len = len(queue)

            for _ in range(queue_len):
                curr_node = queue.popleft()
                curr_lst.append(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            if not left:
                res.append(curr_lst)
                left = True
            else:
                curr_lst = curr_lst[::-1]
                res.append(curr_lst)
                left = False
        
        return res

        