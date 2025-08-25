class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_graph = defaultdict(list)
        indeg = [0] * numCourses

        for (course, prereq) in prerequisites:
            course_graph[prereq].append(course)
            indeg[course] += 1

        queue = deque()
        course_count = 0
        res_list = []
        for i in range(numCourses):
            if indeg[i] == 0:
                queue.append(i) 

        while queue:
            curr_course = queue.popleft()
            res_list.append(curr_course)
            course_count += 1

            for next_course in course_graph[curr_course]:
                indeg[next_course] -= 1

                if indeg[next_course] == 0:
                    queue.append(next_course)

        return [] if course_count != numCourses else res_list

