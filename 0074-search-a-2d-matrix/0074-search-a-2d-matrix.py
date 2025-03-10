class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # happy case 
        # input: matrix = [[1,2],[3,4]], target: 2
        # output: true

        # input: matrix = [[1,2],[3,4]], target: 5
        # output: false

        # edge case
        # input: matrix = [[1]], target = 1
        # output: true

        # input: matrix = [[1], [2]], target = 2
        # output: true

        # input: matrix = [[1,2]], target = 1
        # output: true

        # Brute Force - O(n^2)
        # Binary Search 1- O(mlogn)
        # Binary Search - O(log (m*n))

        # m =len(matrix)
        # low, high - 0, m
        # row_to_iterate = 0
        # until low passes high
        #   find the mid index
        #   check if the mid ele is equal to the target
        #       return True
        #   elif mid ele is greater than the target
        #       update high
        #   else: 
        #       row_to_iterate = max(mid, row_to_iterate)
        #       update low    

        # l, r = 0, len(matrix[row_to_iterate])
        # # until low passes high
        #   find the mid index
        #   check if the mid ele is equal to the target
        #       return True
        #   elif mid ele is greater than the target
        #       update l
        #   else: 
        #       update r  

        # return False

        low,high = 0, len(matrix)-1
        row_to_iterate = 0
        while low <= high:
            mid = (low + high) // 2

            if matrix[mid][0] == target:
                return True

            elif matrix[mid][0] > target:
                high = mid - 1

            else:
                row_to_iterate = max(row_to_iterate, mid)
                low = mid + 1

        l, r = 0, len(matrix[row_to_iterate])-1
        while l <= r:
            mid = (l + r) // 2

            if matrix[row_to_iterate][mid] == target:
                return True

            elif matrix[row_to_iterate][mid] > target:
                r = mid - 1

            else:
                l = mid + 1

        return False

        # Time complexity - O(log(m*n))
        # Space complexity - O(1)
    

        
