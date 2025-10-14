# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs
        # queue
        # add the root node to the queue
        # res list

        # until queue is empty

        # get the num of nodes in each layer
        # popped  = False
        # iterate thru that num
            #   pop the ele from the right
            #   if not popped: add it to the res and change it to true
            #   check if there is left subtree
            #       add it to the queue
            #   check if there is right subtree
            #       add it to the queue
        # return the res

        queue = deque()
        res = []

        if not root:
            return res

        queue.append(root)

        while queue:

            right_most = queue[-1]
            res.append(right_most.val)

            length = len(queue)
            for i in range(length):
                cur_node = queue.popleft()
                    
                if cur_node.left:
                    queue.append(cur_node.left)

                if cur_node.right:
                    queue.append(cur_node.right)

        return res

                

                