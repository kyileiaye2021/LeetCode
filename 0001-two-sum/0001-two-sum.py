class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # happy cases
        # input: nums = [2,7,9] , target = 9
        # output: [0,1]

        # input : nums = [1,2,4], target = 5
        # output: [0,2]

        # edge cases
        # input: nums = [1, 1], target = 2
        # output: [0, 1]

        # Brute Force
        # Two pointer with the hashmap

        # low level steps
        # create a hashmap [ele, index]
        # iterate over the list
        #   diff between target and the curr ele
        #   check if the diff is already in hashmap
        #       return a pair of curr ele index and the diff ele index
        #   if not in the hashmap
        #       add the curr ele with its index in the hashmap

        map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in map:
                return [i, map[diff]]

            else:
                map[nums[i]] = i
