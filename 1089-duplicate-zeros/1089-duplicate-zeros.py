class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        # happy cases
        # arr = [1,0,2,3,0,4,5,0]
        # output = [1,0,0,2,3,0,0,4]

        # arr = [0,0,1,2,3]
        # output: [0,0,0,0,1]

        # arr = [1,2,-1]
        # output: [1,2,-1]

        # edge cases
        # arr = [0,0,0]
        # output: [0,0,0]

        # arr = [0]
        # output: [0]

        # [0,1,2,3]
        # [1,2,3]

        n = len(arr)
        ele_count = Counter(arr)
        zero_count = ele_count[0]
        j = n + zero_count - 1
        i = n - 1

        while i >= 0:

            if j < n:
                arr[j] = arr[i]
            j -= 1

            # if ith ele is 0, we need 2 position
            if arr[i] == 0:
                if j < n:
                    arr[j] = 0
                
                j -= 1

            i -= 1
