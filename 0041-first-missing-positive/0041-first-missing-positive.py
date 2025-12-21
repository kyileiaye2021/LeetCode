class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # happy cases
        # nums = [1,2,4]
        # output: 3

        # nums = [-2,2,1,4]
        # output: 3

        # nums = [1,2,3]
        # output: 4

        # edge cases
        # nums = [0, 0]
        # output: 1

        # nums = [-1,-5,-2,-4]
        # output: 1

        # nums = [12, 6, 9]
        # output: 1

        # get the largest num 
        # in the range [1, largest], first missing ele
        # convert nums to set
        # iterate from 1 to largest
        #   check if the curr ele not in nums set
        #       return it
        # O(k + n) time and O(n) space

        # largest = max(nums)
        # smallest = largest + 1
        # num_set = set(nums)
        # for i in range(1, largest + 1):
        #     if i not in num_set:
        #         return i

        # return smallest if smallest > 0 else 1


        # mark all irrelevant ele as n + 1
        # neg ele, 0, and n + 1 eles
        # mark all ele as neg where the corresponding index exist
        # index of the pos num is where the missing num

        n = len(nums)
        smallest = n + 1

        # marking irrelevant eles (neg ele, 0, n + 1 eles) as n + 1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        # finding first missing val by markng the ele as neg in the pos of the indices corresponding with the ele existed in the nums
        for i in range(n):
            if abs(nums[i]) > 0 and abs(nums[i]) <= n:
                visited_index = abs(nums[i]) - 1
                nums[visited_index] = -abs(nums[visited_index])
        
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return smallest
