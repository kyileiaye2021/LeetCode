# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # happy cases
        # input: 1
        #       / \
        #      3.  2
        #     /     \
        #    4       5
        # output: 4

        # input: 1
        #       / \
        #      3   2
        #     / \   
        #    4   5
        # output: 2   

        # input: 1
        #       / \
        #      3   2
        #     /   
        #    4
        # output: 2  

        # edge cases
        # input: 1
        # output: 1

        # input: []
        # output: 0
        
        # BFS
        # for non-null ending nodes, we can maintain their positions by assigning numbers
        # for tracking the first node in each level, we can maintain prevLevel and currLevel 
        # then if currlevel > prevLevel --> update prevLevel and prevNode
        max_len = float('-inf')
        queue = collections.deque()
        queue.append([root, 1, 0]) # [node, num, level]
        prevNum = 1
        prevLevel = 0
        
        while queue:
            node, num, level = queue.popleft()

            if level > prevLevel:
                prevLevel = level
                prevNum = num

            first_node = prevNum # here, prevNum is the first node in each level
            curr_len = (num - first_node) + 1
            max_len = max(max_len, curr_len)

            if node.left:
                queue.append([node.left, num * 2, level + 1])
            if node.right:
                queue.append([node.right, (num * 2) + 1, level + 1])

        return max_len
