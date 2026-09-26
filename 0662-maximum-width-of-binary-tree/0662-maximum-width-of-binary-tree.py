# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        # bfs
        # deque 
        if not root:
            return 0
        dq = collections.deque()
        dq.append((root, 0))
        max_len = float('-inf')

        while dq:
            cur_len = len(dq)
            first_index = dq[0][1]
            last_index = dq[-1][1]
            max_len = max(max_len, last_index - first_index + 1)

            for _ in range(cur_len):
        
                curr_node, index = dq.popleft()
                
                if curr_node.left:
                    dq.append((curr_node.left, index * 2))

                if curr_node.right:
                    dq.append((curr_node.right, index * 2 + 1))

        return max_len
            
            
