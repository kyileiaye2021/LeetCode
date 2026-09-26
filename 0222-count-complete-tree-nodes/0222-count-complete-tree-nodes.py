# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        # find the max height by going to left subtree at each recursive step
        # find num of nodes on height - 1 so far
        # there are 2^h - 1 nodes in the last level
        # if h = 2, there are 0,1,2,3
        # True, true, true, false

        # use binary search to find each index 
        # find in the tree that that index is none or not

        if not root:
            return 0

        def dfs_height(root):
            # base case
            if not root:
                return 0
            # recursive case
            return 1 + dfs_height(root.left)

        def exist(index, height, root):
            l = 0
            r = 2 ** height - 1

            for _ in range(height):
                mid = (l + r) // 2

                if index <= mid:# this index is on the left side
                    root = root.left
                    r = mid
                
                else:
                    root = root.right
                    l = mid + 1

            return root != None

        height = dfs_height(root) - 1

        total_nodes_except_last_level = 2 ** (height) - 1

        # finding the start position at the last level where the node becomes none
        possible = 2 ** (height) # if tree is total complete, this is possible num of nodes 

        l = 0
        r = possible - 1
        start = -1

        while l <= r:
            mid = l + ((r - l) // 2)

            if exist(mid, height, root):
                l = mid + 1

            else:
                start = mid
                print(start)
                r = mid - 1

        count_on_last_level = start if start != -1 else possible 
        print(total_nodes_except_last_level)
        print(count_on_last_level)
        return total_nodes_except_last_level + count_on_last_level
                

