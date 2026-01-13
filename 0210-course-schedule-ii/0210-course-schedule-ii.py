class Solution:
    def dfs(self, curr_course, course_graph, curr_path, course_taken, res):
        if curr_course in curr_path:
            return False
        if curr_course in course_taken:
            return True

        curr_path.add(curr_course)

        for next_course in course_graph[curr_course]:
            if self.dfs(next_course, course_graph, curr_path, course_taken, res) == False:
                return False
        
        curr_path.remove(curr_course)
        course_taken.add(curr_course)
        res.append(curr_course)
        return True
        
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort - O(V + E) time and O(V) space
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

        # indeg = [0] * numCourses
        # res = []
        # course_graph = defaultdict(list)
        # queue = deque()

        # for next_course, prereq in prerequisites:
        #     course_graph[prereq].append(next_course)
        #     indeg[next_course] += 1

        # for course, preq_count in enumerate(indeg):
        #     if preq_count == 0:
        #         queue.append(course)

        # while queue:
        #     curr_course = queue.popleft()
        #     res.append(curr_course)
        #     for next_course in course_graph[curr_course]:
        #         indeg[next_course] -= 1
        #         if indeg[next_course] == 0:
        #             queue.append(next_course)

        # return res if len(res) == numCourses else []

        # DFS for topological sort
        # dfs
        # if it is in the curr path
        #   return []
        # if it is visited
        #   return none
        # add the node to the curr path
        # go to the next courses
        #   call dfs on next course
        # mark it as visited
        # remove from the curr path
        # return [course] + res

        # visited set to keep track of the nodes not to be visited more than once
        # curr path to keep track of the nodes in curr path
        # iterate thru the courses
        #   if it not visited
        #       call dfs on it

        course_graph = defaultdict(list)
        for next_course, prereq in prerequisites:
            course_graph[prereq].append(next_course)

        curr_path = set()
        course_taken = set()
        res = []
        for course in range(numCourses):
            if self.dfs(course, course_graph, curr_path, course_taken, res) == False:
                return []
        return res[::-1]
         
