class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        # a/b = 2
        # b/c = 3
        # a/c = 2 * 3 = 6

        # a --> b --> c # weighted directed graph
        #   2     3

        # {a : (b, div val)
        #  b: [(a, 1/div val), (c, div val)}
        #  c: [(b, 1/div val)]}

        # queue 
        # while queue
        #   pop out the cur ele with div val
        #   mark the cur ele as visited
        #   check if we reach the target
        #       return w
        #   go to nei 
        #       if nei not visited
        #       add it to queue

        hashmap = defaultdict(list)
        for i, eq in enumerate(equations):
            src, target = eq
            hashmap[src].append([target, values[i]])
            hashmap[target].append([src, 1/values[i]])

        def bfs(src, target):
            if src not in hashmap or target not in hashmap:
                return -1
            visited = set()
            queue = deque()
            queue.append((src, 1))

            while queue:
                n, w = queue.popleft()
                visited.add(n)
                if n == target:
                    return w

                for nei in hashmap[n]:
                    cur, val = nei
                    if cur not in visited:
                        queue.append((cur, w * val))

            return -1
        res = []
        for src, target in queries:
            res.append(bfs(src, target))

        return res





