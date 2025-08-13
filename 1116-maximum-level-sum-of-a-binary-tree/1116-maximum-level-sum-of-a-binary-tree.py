# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # input: [1]
        # output: 1

        # input: [1, 2, null]
        # output: 2

        # input: [5, 2, 1]
        # output: 1

        # bfs
        # level_num 
        # max_sum
        queue = collections.deque()
        queue.append((root, 1))
        max_level_num = 1

        max_sum = float('-inf')

        while queue:
            level_len = len(queue)
            curr_level_sum = 0

            for i in range(level_len):
                curr_node, curr_level_num = queue.popleft()
                curr_level_sum += curr_node.val

                if curr_node.left:
                    queue.append((curr_node.left, curr_level_num + 1))

                if curr_node.right:
                    queue.append((curr_node.right, curr_level_num + 1))

            if curr_level_sum > max_sum:
                max_sum = curr_level_sum
                max_level_num = curr_level_num

        return max_level_num
