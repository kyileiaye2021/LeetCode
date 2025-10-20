"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def dfs(self, node, hashmap):
        # base case
        if node in hashmap:
            return hashmap[node]

        copy = Node(node.val)
        hashmap[node] = copy

        for nei in node.neighbors:
            copy.neighbors.append(self.dfs(nei, hashmap))
        return copy

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # hashmap to store the nodes {old node : new copy node}
        # dfs
        hashmap = {}
        return self.dfs(node, hashmap) if node else None
        