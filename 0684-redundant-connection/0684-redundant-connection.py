class Solution:
    def bfs(self, x, target, graph):
        visited = set()
        queue = deque()
        queue.append((x, None))
        visited.add(x)

        while queue:
            curr, parent = queue.popleft()
            if curr == target:
                return True

            for neighbor in graph[curr]:

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, curr))

                elif neighbor != parent:
                    continue
                
        return False

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # no two parents for a child
        # graph
        # {node : [children]}

        # bfs
        # add node 1 along with parent (none) to queue

        # until queue is empty
        #   pop out the node from qaueue
        #   go to the neighbors
        #       if neighbor is in visited
        #           if neighbor is parent: continue
        #           else: return the curr edge
        #       else: add the neighbor to the queue

        graph = defaultdict(list)
        for x, y in edges:
            if x in graph and y in graph and self.bfs(x, y, graph):
                return [x, y]
            graph[x].append(y)
            graph[y].append(x)
        # return []
                
            

