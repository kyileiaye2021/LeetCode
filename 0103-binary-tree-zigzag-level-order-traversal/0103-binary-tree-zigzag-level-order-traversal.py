# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        # bfs
        dq = collections.deque()
        if not root:
            return []

        dq.append(root)
        res = []
        alternate = False
        while dq:
            dq_len = len(dq)
            cur_lst = []
            for _ in range(dq_len):
                if not alternate:
                    curNode = dq.popleft()
                    cur_lst.append(curNode.val)
                    if curNode.left:
                        dq.append(curNode.left)
                    if curNode.right:
                        dq.append(curNode.right)

                if alternate: 
                    curNode = dq.pop()
                    cur_lst.append(curNode.val)
                    if curNode.right:
                        dq.appendleft(curNode.right)
                    if curNode.left:
                        dq.appendleft(curNode.left)
            res.append(cur_lst)
            alternate = True if not alternate else False

        return res

