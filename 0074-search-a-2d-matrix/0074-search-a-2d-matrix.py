class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # first find the row 
        # find the target in that row

        i = 0
        j = len(matrix) - 1

        while i <= j:
            mid = (i + j) // 2
            if matrix[mid][0] == target:
                return True

            elif matrix[mid][0] > target:
                j = mid - 1

            else:
                i = mid + 1

        if j < 0 or j >= len(matrix):
            return False

        l = 0 
        r = len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2

            if matrix[j][mid] == target:
                return True
            
            elif matrix[j][mid] < target:
                l = mid + 1

            else:
                r = mid - 1
            
        return False
    
