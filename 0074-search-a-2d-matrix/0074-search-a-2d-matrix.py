class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first find the row 
        # binary search in that row

        # t = 0
        # bottom = len(matrix)
        # while t <= b:
        #   mid = t + b // 2
        #   if mid ele == target:
        #       row = mid
        #   elif mid ele > target:
        #       b = mid - 1
        #   else
        #       t = mid

        # l = row
        # r =  row + col

        # while l <= r:
        # mid = l + r // 2
        # if mid ele < target:
        #   l = mid + 1
        # elif mid ele > target:
        #   r = mid - 1
        # else
        #   return True

        # return False

        t = 0
        b = len(matrix) - 1
        row = 0
        while t <= b:
            mid = (t + b) // 2

            if matrix[mid][0] == target:
                return True

            elif matrix[mid][0] > target:
                b = mid - 1

            else:
                row = mid
                t = mid + 1

        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            print(mid)

            if matrix[row][mid] > target:
                r = mid - 1
            
            elif matrix[row][mid] < target:
                l = mid + 1

            else:
                return True

        return False

            

