class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        row = 0
        while l <= r:
            mid = (l + r) // 2

            if matrix[mid][0] == target:
                return True

            elif matrix[mid][0] > target:
                r = mid - 1

            else:
                row = mid
                l = mid + 1

        
        i = 0
        j = len(matrix[0]) - 1
        while i <= j:
            mid = (i + j) // 2

            if matrix[row][mid] == target:
                return True

            elif matrix[row][mid] > target:
                j = mid - 1

            else:
                i = mid + 1

        return False
    
