class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # preq_map {preq -> course}
        # indeg {course -> num of preq}

        # queue
        # add the course with no preq in the queue
        # until queue is empty
        #   pop out the cur course
        #   go to courses that need cur course as prereq
        #       decrement the indeg of nei course
        #       if nei course indeg == 0
        #           add nei course to queue
        # check every indeg of courses becomes 0 --> return true else false

        preq_map = defaultdict(set)
        indeg = [0] * numCourses

        for c, p in prerequisites:
            preq_map[p].add(c)
            indeg[c] += 1

        queue = deque()
        for i, ind in enumerate(indeg):
            if ind == 0:
                queue.append(i)

        while queue:
            cur_course = queue.popleft()
            numCourses -= 1
            if numCourses == 0:
                return True

            for nei in preq_map[cur_course]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    queue.append(nei)

        
        return True if numCourses == 0 else False

            





