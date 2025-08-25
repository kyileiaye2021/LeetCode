class Solution:
    def dfs(self, visited, graph, currcity, count):
        visited.add(currcity)

        for (neighbor, tag) in graph[currcity]:
            if neighbor not in visited:
                if tag == 1:
                    count[0] += 1
                self.dfs(visited, graph, neighbor, count)


    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()
        graph = defaultdict(list)
        count = [0]

        for x, y in connections:
            graph[x].append((y, 1))
            graph[y].append((x, -1))

        print(graph)

        self.dfs(visited, graph, 0, count)
        return count[0]




    