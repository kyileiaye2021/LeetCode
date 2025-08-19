class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = collections.deque()
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])
        
        minute = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if not fresh:
            return 0
        
        while queue:
            queue_len = len(queue)
            
            for _ in range(queue_len):
                r,c = queue.popleft()
                
                for dx,dy in dir:
                    nr = r+dx
                    nc = c+dy
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        fresh -= 1
                        queue.append((nr,nc))
            minute += 1
        
        return -1 if fresh > 0 else minute-1