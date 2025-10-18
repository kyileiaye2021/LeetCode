class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # total = first ele in nums
        # iterate thru the nums upto last index
        #   decrement 1 step from total
        #   if total < 0:
        #       return False
        #   if total == 0
        #       add curr jump len to total
        # if total >= 0 -> we can reach to the end
        
        total = nums[0]
        for i in range(0, len(nums) - 1):
            if total < 0:
                return False
            if nums[i] > total:
                total = nums[i]
            total -= 1

        return True if total >= 0 else False

       