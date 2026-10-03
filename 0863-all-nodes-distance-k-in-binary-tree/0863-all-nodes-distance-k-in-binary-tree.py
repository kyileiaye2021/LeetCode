# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
       
        # need to go up and down k dist from target
        # undirected graph from node 5
        # create a hashmap
        # add node 5 to queue
        #   pop its nei for k times

        parent = {}
        dq = collections.deque()
        
        def dfs(root, p):
            if not root:
                return 

            if root == target:
                dq.append(root)
            
            parent[root] = p
            dfs(root.left, root)
            dfs(root.right, root)

        dfs(root, None)
        visited = set()

        i = 0
        while dq and i < k:
            dq_len = len(dq)
            for _ in range(dq_len):
                cur_node = dq.popleft()
                visited.add(cur_node)
                if cur_node.left and cur_node.left not in visited:
                    dq.append(cur_node.left)
                if cur_node.right and cur_node.right not in visited:
                    dq.append(cur_node.right)
                if parent[cur_node] and parent[cur_node] not in visited:
                    dq.append(parent[cur_node])
            i += 1

        return [node.val for node in dq]
        








