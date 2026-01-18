# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # DFS
        # create parent graph with dfs
        # 
        if not root:
            return []
        parent = {}
        def create_graph(root, parent_node=None):
            if not root:
                return

            parent[root] = parent_node
            create_graph(root.left, root)
            create_graph(root.right, root)
        
        create_graph(root)

        # print(parent)
        visited = set()
        res = []

        def dfs(root, k):
            # base case
            if root in visited or not root:
                return
            
            visited.add(root)
            if k == 0:
                res.append(root.val)

            # recursive case
            dfs(root.left, k - 1)
            dfs(root.right, k - 1)
            dfs(parent[root], k - 1)

        dfs(target, k)
        return res

        # # first we have to create a map that maps to children to their parent
        # # queue to iterate all nodes and add their parent-child relationship
        # # visited
        # # queue and add the target node
        # # while k > 0 and queuE isn't empty
        # #   iterate thru the queue len
        # #       check if there is left child of the curr node
        # #           if it's not in the visited
        # #               add it to the queue
        # #       if there is right child
        # #           if it's not in the visited
        # #               add it to the queue
        # #       if there is parent
        # #           if it's not in the visited
        # #               add it to the queue
        # # return list(queue)


        # queue = deque() #{child node val: parent node}
        # queue.append(root)
        # parent = defaultdict()

        # while queue:
        #     for _ in range(len(queue)):
        #         curr = queue.popleft()
                
        #         if curr.left:
        #             parent[curr.left] = curr
        #             queue.append(curr.left)

        #         if curr.right:
        #             parent[curr.right] = curr
        #             queue.append(curr.right)
                
        
        # queue = deque() 
        # queue.append(target)
        # visited = set()

        # while k > 0 and queue:
        #     for _ in range(len(queue)):
        #         curr = queue.popleft()
        #         visited.add(curr)

        #         if curr.left and curr.left not in visited:
        #             queue.append(curr.left)
                
        #         if curr.right and curr.right not in visited:
        #             queue.append(curr.right)
                
        #         if curr in parent and parent[curr] not in visited:
        #             queue.append(parent[curr])

        #     k -= 1

        # res = []
        # while queue:
        #     res.append(queue.popleft().val)
        # return res
