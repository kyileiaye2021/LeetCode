class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        terminal_map = defaultdict(set)
        outdeg = [0] * len(graph)

        for i, nodes in enumerate(graph):
            for n in nodes:
                terminal_map[n].add(i)
                outdeg[i] += 1

        queue = deque()
        for i, out in enumerate(outdeg):
            if out == 0:
                queue.append(i)

        res = []
        while queue:
            cur_node = queue.popleft()
            res.append(cur_node)
            for nei in terminal_map[cur_node]:
                outdeg[nei] -= 1

                if outdeg[nei] == 0:
                    queue.append(nei)

        return sorted(res)


