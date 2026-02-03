class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # col set 
        # diagonal set
        # antidiagnoal set
        
        # create a empty nxn graph
        # iterate thru the rows
        #   check if curr col is not in col set
        #       add the Q to the curr row and col
        #       add the col to col set
        #   calculate diagonal and anti-diag coordinates
        #   check if diag and anti-diag is not in diag and antidiag sets
        #       add them to diag and antidiag sets
        
        # (0,0), (1,1), (2,2) 
        
        # dfs
        # iterate thru the cols
        #   call dfs to go to next row
        #  
        
        # ["..Q.","Q...","...Q",".Q.."]
        matrix = [['.'] * n for r in range(n)]
        col_set = set()
        diag_set = set()
        anti_diag = set()
        res = []
        
        def dfs(r):
            
            # base case
            if r == n:
                res.append([''.join(r) for r in matrix])
            
            for c in range(n):
                
                if c not in col_set and r - c not in diag_set and r + c not in anti_diag:
                    matrix[r][c] = 'Q'
                    col_set.add(c)
                    diag_set.add(r - c)
                    anti_diag.add(r + c)
                    
                    dfs(r + 1)
                    
                    col_set.remove(c)
                    diag_set.remove(r - c)
                    anti_diag.remove(r + c)
                    matrix[r][c] = '.'
            
        dfs(0)        
        return res
                    
                    
            
            
            