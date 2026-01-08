# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        # bfs
        # deque
        # add the root node to the deque
        # res

        # until deque is empty
        #   len of the curr deque
        #   cur sum = 0
        #   iterate thru the deque that times
        #       pop out the curr node
        #       add the curr node val to the cur sum
        #       if there are leeft and right children , add them to the deque
        #   add the cur sum / len to res
        # return res

        q = collections.deque()
        q.append(root)
        res = []

        while q:
            curr_len = len(q)
            curr_sum = 0

            for _ in range(curr_len):
                curr_node = q.popleft()
                curr_sum += curr_node.val

                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)

            avg = curr_sum / curr_len
            res.append(avg)

        return res