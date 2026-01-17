# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # first we have to create a map that maps to children to their parent
        # queue to iterate all nodes and add their parent-child relationship
        # visited
        # queue and add the target node
        # while k > 0 and queuE isn't empty
        #   iterate thru the queue len
        #       check if there is left child of the curr node
        #           if it's not in the visited
        #               add it to the queue
        #       if there is right child
        #           if it's not in the visited
        #               add it to the queue
        #       if there is parent
        #           if it's not in the visited
        #               add it to the queue
        # return list(queue)


        queue = deque() #{child node val: parent node}
        queue.append(root)
        parent = defaultdict()

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                
                if curr.left:
                    parent[curr.left] = curr
                    queue.append(curr.left)

                if curr.right:
                    parent[curr.right] = curr
                    queue.append(curr.right)
                
        
        queue = deque() 
        queue.append(target)
        visited = set()

        while k > 0 and queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                visited.add(curr)

                if curr.left and curr.left not in visited:
                    queue.append(curr.left)
                
                if curr.right and curr.right not in visited:
                    queue.append(curr.right)
                
                if curr in parent and parent[curr] not in visited:
                    queue.append(parent[curr])

            k -= 1

        res = []
        while queue:
            res.append(queue.popleft().val)
        return res
