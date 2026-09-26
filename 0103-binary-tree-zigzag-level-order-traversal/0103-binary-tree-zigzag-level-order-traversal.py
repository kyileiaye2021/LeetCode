# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        
        # bfs
        # if root is none
        #   return none
        # deque 
        # res = 
        # add root to deque
        # pop until dq is empty
        #   len(curr dq)
        #   curr list = []
        #   iterate thru the len of curr dq
        #       pop curr node and add it to curr list
        #       if curr node has left child : add it to queue
        #       if curr node has right child: add it to queue
        #   add curr list to res list
        # return res

        res = []
        if not root:
            return res

        dq = collections.deque()
        dq.append(root)

        left_to_right = True
        while dq:
            curr_len = len(dq)
            curr_lst = []

            for _ in range(curr_len):
                if left_to_right:
                    curr_node = dq.popleft()
                    if curr_node.left:
                        dq.append(curr_node.left)
                    if curr_node.right:
                        dq.append(curr_node.right)
                    
                else:
                    curr_node = dq.pop()
                    if curr_node.right:
                        dq.appendleft(curr_node.right)
                    if curr_node.left:
                        dq.appendleft(curr_node.left)

                curr_lst.append(curr_node.val)
        
            res.append(curr_lst)
            left_to_right = False if left_to_right else True

        return res
                