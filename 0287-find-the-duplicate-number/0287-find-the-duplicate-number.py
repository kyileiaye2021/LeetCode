class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # XOR??
        # nums = [1,3,2,4,2]
        # otuput: 2

        # nums = [1, 1]
        # output: 2

        # nums = [2,2,1]
        # output: 2

        # nums = [1]
        # output: 0

        # nums = [2,2,2,3]
        # output: 2

        # [1,2,3,4] inclusive 1-n
        # [1,2,3,4,2]
        # xor those two arrs, then we are left with the extra one
        # iterate thru the ele in nums:
        #   adding the cur ele and subtract the ele in n_arr
        #   increment pt in n_arr

        # get the index
        # negate the ele at that index
        # if it's already negated
        #   return it
        # negate the ele
        # return 0

        for i in range(len(nums)):
            visited_index = abs(nums[i]) - 1
            if nums[visited_index] < 0:
                return visited_index + 1
            nums[visited_index] = -nums[visited_index]

        return 0
        

        
