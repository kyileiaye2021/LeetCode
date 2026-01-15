# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs
        # queue
        # add the root to the queue
        # pop the curr node until queue is empty
        #   add the popped node to the res
        #   add the children if the curr node has one
        # reverse the res list
        # return the res

        if not root:
            return []
            
        queue = deque()
        queue.append(root)
        res = []

        while queue:
            curr_len = len(queue)
            curr_res = []

            for _ in range(curr_len):
                curr_node = queue.popleft()
                curr_res.append(curr_node.val)
                
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
                
            res.append(curr_res)
        
        return res[::-1]
            