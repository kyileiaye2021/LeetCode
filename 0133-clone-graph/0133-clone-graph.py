"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # happy case
        # input: [[2,4],[1,3],[2,4],[1,3]]
        # output: [[2,4],[1,3],[2,4],[1,3]]

        # input: [[2,3], [1], [1]]

        # edge case
        # input: []
        # output: []

        # input: [[]]
        # output: [[]]

        # bfs
        # queue 
        # hashmap {old node : new node}

        # bfs 
        # create a queue
        # hashmap  {old node: new node}
        # add the first node into the queue
        # add the first node into the hashmap
        # until the queue is empty
        #   pop out the node 
        #   for each neighbor
        #       check if the neighbor node is already not in the hashmap
        #           create a new node
        #           add the new node into the hashmap
        #           add it to the queue
        #           append that node to the curr neighbor's list
        #        if the neighbor is already in the hashmap
        #           append that node to the curr neighbor's list

        queue = collections.deque()
        oldToNew = {}

        if not node:
            return None

        queue.append(node)
        new_node = Node(node.val, [])
        oldToNew[node] = new_node

        while queue:
            curr_node = queue.popleft()
            
            cloned_node = oldToNew[curr_node]

            for nei in curr_node.neighbors:

                if nei not in oldToNew:

                    # make a new node and mark it as cloned
                    new_nei = Node(nei.val, [])
                    oldToNew[nei] = new_nei

                    queue.append(nei)

                cloned_node.neighbors.append(oldToNew[nei])

        return oldToNew[node]