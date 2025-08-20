class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # iterate thru each city
        #   dfs() on eaach city
        
        
        # in dfs
        #   go to neighbors
        #   backtrack and change edges
        #   count the edges as well
        
        # creating a graph
        # [[0, 1]
        #   [0, 1]]
        
        def dfs(curcity):
            visited.add(curcity)
            nonlocal changes
            
            for (neighbor, tag) in adj[curcity]:
                if neighbor not in visited:
                    if tag == 1:
                        changes += 1
                    dfs(neighbor)
            
        
        adj = [[] for _ in range(n)]
        
        for (u, v) in connections:
            adj[u].append((v, 1)) # going away from city 0
            adj[v].append((u, -1)) # going towards city 0
            
        print(adj)
        
        visited = set()
        changes = 0
        dfs(0)
        return changes
        
