class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # happy cases
        # nums = [2,7,11,15], target = 9
        # [0, 1]

        # nums = [3,2,4], target = 6
        # [1,2]

        # edge cases
        # nums = [], target = 9
        # []

        # nums = [1,2,3], target = 9
        # []

        # nums = [1,-2], target = 1
        # []

        # hashmap : {curr ele: curr ele index}

        hashmap = {}

        for i, n in enumerate(nums):
            # print(hashmap)
            pair = target - n
            if pair in hashmap:
                return [i, hashmap[pair]]
            
            hashmap[n] = i

        return []
        




