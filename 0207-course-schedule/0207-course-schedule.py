class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # topological sort
        # indegree array [0] * n

        # {course : next courses}
        # iterate (next, prereq) thru the pairs in prereq
        #   indegree[next] += 1

        # bfs
        # queue
        # add the courses with no prereq to the queue

        # iterate thru the 0 - n - 1 courses
        #   check if the curr course is not in the next course values
        #       add them to the queue
        #       numCourse -= 1

        # until queue is empty
        #   pop out those courses
        #   go to next courses
        #       decrement the indegree
        #       check if indegree becomes 0
        #           add the next course in queue
        #           numCourses -= 1

        # return true if numCourses == 0 else return false

        course_map = defaultdict(list)
        indegree = [0] * numCourses
        for next_course, prereq in prerequisites:
            course_map[prereq].append(next_course)
            indegree[next_course] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                numCourses -= 1

        while queue:
            curr_course = queue.popleft()
            for next_course in course_map[curr_course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
                    numCourses -= 1

        return True if numCourses == 0 else False
        



