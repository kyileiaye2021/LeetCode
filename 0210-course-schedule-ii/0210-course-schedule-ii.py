class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq_map = defaultdict(set)
        indeg = [0] * numCourses
        res = []

        for c, p in prerequisites:
            preq_map[p].add(c)
            indeg[c] += 1

        queue = deque()
        for i, ind in enumerate(indeg):
            if ind == 0:
                queue.append(i)

        while queue:
            cur_course = queue.popleft()
            res.append(cur_course)
            numCourses -= 1
            if numCourses == 0:
                return res

            for nei in preq_map[cur_course]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    queue.append(nei)

        
        return res if numCourses == 0 else []