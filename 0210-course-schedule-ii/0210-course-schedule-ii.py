class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort
        # indeg arr - a list of num of indeg or prereq for each course
        # res = []

        # graph that maps to the prereq course to next coures
        # queue
        # add all courses with no indeg to the queue
        # until the queue is empty
        #   pop the queue
        #   add the course to the res
        #   iterate thru the next course
        #       decrement their indeg
        #       if their indeg is 0, add the course to the queue
        # return res if len of res == numcourses

        indeg = [0] * numCourses
        res = []
        course_graph = defaultdict(list)
        queue = deque()

        for next_course, prereq in prerequisites:
            course_graph[prereq].append(next_course)
            indeg[next_course] += 1

        for course, preq_count in enumerate(indeg):
            if preq_count == 0:
                queue.append(course)

        while queue:
            curr_course = queue.popleft()
            res.append(curr_course)
            for next_course in course_graph[curr_course]:
                indeg[next_course] -= 1
                if indeg[next_course] == 0:
                    queue.append(next_course)

        return res if len(res) == numCourses else []
