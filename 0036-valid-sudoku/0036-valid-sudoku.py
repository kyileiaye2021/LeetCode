class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows_hashmap = defaultdict(set)
        cols_hashmap = defaultdict(set)
        subgroup_hashmap = defaultdict(set)
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == '.':
                    continue
                new_r, new_c = r // 3, c // 3
                if board[r][c] in rows_hashmap[r] or board[r][c] in cols_hashmap[c] or board[r][c] in subgroup_hashmap[(new_r, new_c)]:
                    return False

                rows_hashmap[r].add(board[r][c])
                cols_hashmap[c].add(board[r][c])
                subgroup_hashmap[(new_r, new_c)].add(board[r][c])

        return True

        