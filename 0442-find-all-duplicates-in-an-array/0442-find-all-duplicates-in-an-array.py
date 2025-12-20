class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # get the indices of the ele that are part of the ele
        # at those indices negate the ele
        # if the ele is already negative
        #   add the index to the res
        # negate the ele
        # +1 to each ele of res and return the res
        res = []
        for i in range(len(nums)):
            visited_index = abs(nums[i]) - 1
            if nums[visited_index] < 0:
                res.append(visited_index + 1)
            nums[visited_index] = -nums[visited_index]

        return res
