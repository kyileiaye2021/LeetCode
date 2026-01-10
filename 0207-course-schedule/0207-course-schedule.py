class Solution:
    def dfs(self, curr_course, preq_graph, visited, curr_visited):
        if curr_course in curr_visited:
            return False

        if curr_course in visited:
            return True

        curr_visited.add(curr_course)

        for next_course in preq_graph[curr_course]:
            if not self.dfs(next_course, preq_graph, visited, curr_visited):
                return False
    
        curr_visited.remove(curr_course)
        # mark the node as visited
        visited.add(curr_course)
        return True
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #DFS
        # graph {preq: next courses}
        # visted to keep track of which nodes are already visited
        # curr visited to keep track of visited nodes in each curr path
        preq_graph = defaultdict(list)
        visited = set()
        curr_visited = set()

        for next_course, preq in prerequisites:
            preq_graph[preq].append(next_course)

        for i in range(numCourses):
            if i not in visited:
                if not self.dfs(i, preq_graph, visited, curr_visited):
                    return False
        
        return True


        # create a graph for numCOurses
        # processed_courses = 0
        # preq_graph = defaultdict(list)
        # in_deg_graph = defaultdict(list)

        # for next_course, preq in prerequisites:
        #     preq_graph[preq].append(next_course)
        #     in_deg_graph[next_course].append(preq)
        
        # # keep track of in-degrees for each course
        # in_deg = [0] * numCourses
        # for course in range(numCourses):
        #     for _ in in_deg_graph[course]:
        #         in_deg[course] += 1

        # # queue to add all courses with no in-deg
        # # if queue is empty -> return false
        # queue = deque()
        # for course in range(numCourses):
        #     if in_deg[course] == 0:
        #         queue.append(course)
        #         processed_courses += 1

        # if not queue:
        #     return False

        # # whiile queue is not empty
        # #   pop out the queue
        # #   itreate thru the next coures of that course
        # #       decrement the indeg of the next courese
        # #       if in-deg of next course becomes 0
        # #           add it to the queue
        # while queue:
        #     curr_course = queue.popleft()
        #     for next_course in preq_graph[curr_course]:
        #         in_deg[next_course] -= 1
        #         if in_deg[next_course] == 0:
        #             queue.append(next_course)
        #             processed_courses += 1

        # return True if processed_courses == numCourses else False

