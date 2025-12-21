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

        largest = max(nums)
        smallest = largest + 1
        num_set = set(nums)
        for i in range(1, largest + 1):
            if i not in num_set:
                return i

        return smallest if smallest > 0 else 1
