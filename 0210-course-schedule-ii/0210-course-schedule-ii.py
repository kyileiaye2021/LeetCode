class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # bfs
        
        # hashmap {preq: courses}
        indeg = [0] * numCourses
        course_graph = defaultdict(list)
        for (course, prereq) in prerequisites:
            course_graph[prereq].append(course)
            indeg[course] += 1
        
        course_res = []
        queue = collections.deque()
        # store the course with no prereq in the queue first
        for i in range(numCourses):
            if indeg[i] == 0:
                queue.append(i)
            
        while queue:
            
            curr_course = queue.popleft()
            course_res.append(curr_course)
            
            for next_course in course_graph[curr_course]:
                indeg[next_course] -= 1
                
                if indeg[next_course] == 0:
                    queue.append(next_course)
        
        return course_res if len(course_res) == numCourses else []
        
        
        
        
        # graph = {i: [] for i in range(numCourses)}
        # dependences = defaultdict(list)
        
        # order = []
        
        # for course, prereq in prerequisites:
        #     graph[course].append(prereq)
        #     dependences[prereq].append(course)
            
        # independent = [i for i in graph if not graph[i]]
        # queue = deque(independent)
        
        # while queue:
        #     cur = queue.popleft()
        #     order.append(cur)
            
        #     for nextLevelCourse in dependences[cur]:
        #         graph[nextLevelCourse].remove(cur)
        #         if not graph[nextLevelCourse]:
        #             queue.append(nextLevelCourse)
            
        #     graph.pop(cur)
        
        # return order if not graph else []        
        
        
        