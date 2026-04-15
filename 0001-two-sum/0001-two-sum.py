class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap
        # iterate thru the ele 
        #   diff = subtract the cur ele from target
        #   check if the diff in hashmap
        #       return [cur ele idx, diff idx]
        #   else
        #       add the [curr ele : curr idx]

        hashmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [i, hashmap[diff]]
            else:
                hashmap[n] = i

            