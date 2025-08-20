class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # dfs 
        # make a undirected graph
        # isConnected = [[1,1,0]
        #                [1,1,0]
        #                [0,0,1]]
        # output = 2
        
        # isConnected = [[1,0,0]
        #                [0,1,0]
        #                [0,0,1]]
        # output = 3
        
        # use set to collect all nodes visited.
        # use a nested for loop, iterate through all elements
        # if current index is not visited, then we need to call dfs
        
        # one city is always connected to itself, so it will have at most n provices
        # so we increse the number by one, each time we check with this city, and then try to find all adjacent cities, and mark them as visited
        
        def dfs(i):
            visited.add(i)
            
            for j in range(rows):
                if j not in visited and isConnected[i][j] == 1:
                    dfs(j)
        
        
        rows = len(isConnected)
        cols = len(isConnected[0])
        province = 0
        visited = set()
        
        for i in range(rows):
            if i not in visited:
                province += 1
                dfs(i)
                
                    
        # isConnected[r][c] = isConnected[c][r], we only have n cities
        
        return province
        
        