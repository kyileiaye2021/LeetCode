# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #BFS
        # if not root:
        #     return []
            
        # queue = deque()
        # queue.append(root)
        # res = []

        # while queue:
        #     curr_len = len(queue)
        #     last_node = queue[-1]
        #     res.append(last_node.val)

        #     for _ in range(curr_len):
        #         curr_node = queue.popleft()
                
        #         if curr_node.left:
        #             queue.append(curr_node.left)
        #         if curr_node.right:
        #             queue.append(curr_node.right)
                
        # return res

        #DFS
        # base case: if node is null
        # return 
        # if the first node at that level save the node val. in the res list
        # go to right subtree first then left
        res = []
        def dfs(node, depth):

            if not node:
                return

            if depth == len(res):
                res.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0) 
        return res
            
        