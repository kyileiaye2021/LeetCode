class Solution:
    def dfs(self, i, graph, map):
        # if i already in the map
        #   return node's safe status

        # add i to map with the status of false

        # for nei in curr's neighors
        #   status = call dfs(nei, graph, map)
        #   if status is not true 
        #       return False
        # map[i] = True
        # return True

        if i in map:
            return map[i]
        
        # add the curr node with the status of False
        map[i] = False

        for nei in graph[i]:
            if not self.dfs(nei, graph, map): # if the nei returns false (not a safe node), then the curr is not the safe node
                return False

        # if all nei are safe node, then the curr is also safe node
        map[i] = True
        return True


    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        map = {}
        res = []
        for i in range(len(graph)):
            if self.dfs(i, graph, map):
                res.append(i)

        return res

