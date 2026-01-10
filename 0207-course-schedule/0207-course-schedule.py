class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create a graph for numCOurses
        processed_courses = 0
        preq_graph = defaultdict(list)
        in_deg_graph = defaultdict(list)

        for next_course, preq in prerequisites:
            preq_graph[preq].append(next_course)
            in_deg_graph[next_course].append(preq)
        
        # keep track of in-degrees for each course
        in_deg = [0] * numCourses
        for course in range(numCourses):
            for _ in in_deg_graph[course]:
                in_deg[course] += 1

        # queue to add all courses with no in-deg
        # if queue is empty -> return false
        queue = deque()
        for course in range(numCourses):
            if in_deg[course] == 0:
                queue.append(course)
                processed_courses += 1

        if not queue:
            return False

        # whiile queue is not empty
        #   pop out the queue
        #   itreate thru the next coures of that course
        #       decrement the indeg of the next courese
        #       if in-deg of next course becomes 0
        #           add it to the queue
        while queue:
            curr_course = queue.popleft()
            for next_course in preq_graph[curr_course]:
                in_deg[next_course] -= 1
                if in_deg[next_course] == 0:
                    queue.append(next_course)
                    processed_courses += 1

        return True if processed_courses == numCourses else False