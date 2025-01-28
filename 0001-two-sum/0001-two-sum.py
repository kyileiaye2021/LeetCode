class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Happy cases
        # input - [2,7,11,15], target = 9
        # output = [0,1]

        # Edge cases
        # input - [3,2], target = 5
        # output = [0, 1]

        # dictionary approach
        # {ele : index}
        # iterate over the ele in the list
        #   do a diff between the target and curr ele
        #       check if the diff is in dict
        #           return the curr ele index and diff ele index as a list
        #       else: add the curr ele with its index in the dict
        
        idx_map = {}
        
        for i, ele in enumerate(nums):
            diff = target - ele
            if diff in idx_map:
                return [i, idx_map[diff]]

            else:
                idx_map[ele] = i

        