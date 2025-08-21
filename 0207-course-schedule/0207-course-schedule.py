class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # array that shows all prerequisites, we can go over the array, to find if there is no prerequistes for a single course.
        # prerequisites = {course: [prerequisites courses]}
        # {prereq: [next courses]}
        # courses = [] all courses that we can take
        
        
        # course_graph = {i: [] for i in range(numCourses)}
        # asPrereq = defaultdict(list)
        
        # for course, prereq in prerequisites:
        #     course_graph[course].append(prereq) # {course: preq}
        #     asPrereq[prereq].append(course)     # {prereq: course}
        
        # queue = deque() # all course we can finish without prerequ
        
        # for c in course_graph:
        #     if not course_graph[c]:
        #         queue.append(c)
        
        # while queue:
            
        #     curr_course = queue.popleft()
            
        #     for nextC in asPrereq[curr_course]:
        #         course_graph[nextC].remove(curr_course)
                
        #         if not course_graph[nextC]:
        #             queue.append(nextC)
            
        #     course_graph.pop(curr_course) # we want to remove the current course from the map, because we want to check whether no course left
            
        # return not course_graph
        
        
        
        course_graph = defaultdict(list) # {prereq: [courses]}
        
        for (course, prereq) in prerequisites:
            course_graph[prereq].append(course)
            
        indeg = [0] * numCourses
    
        for prereq in course_graph:
            for course in course_graph[prereq]:
                indeg[course] += 1
                
        queue = deque()
        
        for i in range(numCourses):
            if indeg[i] == 0:
                queue.append(i)
         
        finish = 0
        while queue:
            cur = queue.popleft()
            finish += 1
            
            for neighbor in course_graph[cur]:
                indeg[neighbor] -= 1
                
                if indeg[neighbor] == 0:
                    queue.append(neighbor)
                    
        return (finish == numCourses)
        
            
        '''
        class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return finish == numCourses
        '''
        
        '''
        graph = {i: [] for i in range(numCourses)} # {course: prerequisites}
        froms = defaultdict(list) # {prerequisites: courses}
        for i, j in prerequisites:
            graph[i].append(j)
            froms[j].append(i)
        
        # all couses that there is no prerequisites
        ends = [i for i in graph if not graph[i]]
        q = deque(ends)
        
        # use bfs
        while q:
            cur = q.popleft()
            
            # iterate through all courses that use cur course as a prerequisite
            for i in froms[cur]:
                # we remove this prerequisite course from the graph of that course
                graph[i].remove(cur)
                
                # if no prerequisite, we simply add to the queue
                if not graph[i]:
                    q.append(i)
            graph.pop(cur)
        
        return not graph
        '''
        
        '''
        class Solution:
    def createGraph(self, prerequisites):
        graph = collections.defaultdict(list)
        for (course, prereq) in prerequisites:
            graph[prereq].append(course)
        return graph        
                                                                                                                                             
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # happy cases
        # input: numCourses = 2, prerequisites = [[0,1], [1,0]]
        # output: false

        # input: numCourses = 3, prerequisites = [[1,0], [2,1]]
        # output: true

        # input: numCourses = 3, prerequisites = [[1,0], [2,0]]
        # output: true

        # edge cases
        # input: numCourses = 1, prerequisites = [[0, None]]
        # output: true

        # graph algorithm
        # topological sort
        # direct graph with bfs
        # create graph func {sec: [first]}
        #   iterate thru the prereq pairs
        #      pair the sec ele to the first ele
        #   return the graph

        # create a graph with pairs
        # keep track of the in degree for nodes
        # create a list of size numCourses all initialized to 0
        # iterate thru the graph
        #   for each value in the list
        #       value is index of the list
        #       increment the in deg num in val index position of the list
        # find the nums that have 0 in deg
        # create queue and add those nums to the queue
        # mark those nums as visited
        # iterate until queue is empty
        # pop out the curr node
        #   iterate each neighbor of curr popped out node
        #      if the neighbor is not visited
        #       decrement the in degree
        #       if in deg becomes 0
        #           add the node to the queue
        course_graph = self.createGraph(prerequisites) {preq: [coureses]}
        in_deg = [0] * numCourses

        for prereq in course_graph:
            for course in course_graph[prereq]:
                in_deg[course] += 1

        queue = collections.deque()
        for i, val in enumerate(in_deg):
            if val == 0:
                queue.append(i)

        count = 0
        while queue:
            prereq = queue.popleft()
            count += 1

            # go to prereq courses
            for course in course_graph[prereq]:
                in_deg[course] -= 1

                if in_deg[course] == 0:
                    queue.append(course)

        return (count == numCourses)       

        '''

        