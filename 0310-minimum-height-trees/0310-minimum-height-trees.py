class Solution:
                
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # create graph using edges
        # iterate thru the nodes
        #   curr_height call bfs func on the node
        #   update the max height and res root if needed
        # return res list
        if n == 1:
            return [0]
        graph = defaultdict(list)
        queue = deque()
        
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        print(graph)

        indeg = [0] * n
        for src, nei in graph.items():
            if len(graph[src]) == 1:
                queue.append(src)
            indeg[src] = len(graph[src])
        
        while queue:
            if n <= 2:
                return list(queue)
            for _ in range(len(queue)):
                curr = queue.popleft()
                n -= 1
                for nei in graph[curr]:
                    indeg[nei] -= 1
                    if indeg[nei] == 1:
                        queue.append(nei)


