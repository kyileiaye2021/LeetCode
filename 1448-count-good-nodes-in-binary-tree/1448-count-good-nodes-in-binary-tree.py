# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # keeping track of max val at each node
        # root node - 3, max_val = 0
        # BFS
        # add the root in the queue (3, 0)
        # pop the node
        # 3 >= 0 --> good increment count
        # update max val for next children --> max(max_val, cur node val)
        # return count

        queue = deque([(root, root.val)])
        count = 0

        while queue:
            cur_node, max_val = queue.popleft()

            if cur_node.val >= max_val:
                count += 1
                max_val = cur_node.val

            if cur_node.left:
                queue.append((cur_node.left, max_val))
            
            if cur_node.right:
                queue.append((cur_node.right, max_val))

        return count



        