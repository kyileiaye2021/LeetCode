class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        N = len(grid)
        count = {}

        for i in range(N):
            for j in range(N):
                if grid[i][j] not in count: 
                    count[grid[i][j]] = 0
                
                count[grid[i][j]] += 1

        missing, repeated = 0, 0

        for i in range(1, N*N + 1):
            if i not in count:
                missing = i

            elif count[i] == 2:
                repeated = i

        return [repeated, missing]

            

        
                 
                
