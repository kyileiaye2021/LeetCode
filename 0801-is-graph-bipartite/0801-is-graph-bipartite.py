class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        # bipartite
        # we have 2 sets
        # we have to check if the node in the same set are neighbor --> not bipartite

        # bfs
        # color = [0] * num of vertices
        # iterate thru every node
        #   add the node to queue if it is not colored yet.
        #       add the node to the queue
        #   until the queue is empty
        #      pop out the curr node
        #      go to nei
        #       if it's not colored yet
        #           colored with another color and add to the queue
        #       if it's already colored
        #           check if the color is the same as curr node
        #               return False
        # return true
        queue = deque()

        color = [-1] * len(graph)

        for i in range(len(graph)):

            if color[i] == -1:
                queue.append(i)
                color[i] = 0

            while queue:
                cur_node = queue.popleft()

                for nei in graph[cur_node]:

                    # if the nei is not colored yet
                    if color[nei] == -1:
                        color[nei] = 1 - color[cur_node]
                        queue.append(nei)
                    
                    # if it's already colored, check if the color is the same as the curr color
                    elif color[nei] == color[cur_node]:
                        return False

        return True



        