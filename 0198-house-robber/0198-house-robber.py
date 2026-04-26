class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[-1]
        first = nums[0]
        second = max(first, nums[1])


        for i in range(2, len(nums)):
            temp = first
            first = second
            if nums[i] + temp > second:
                second = nums[i] + temp
            
        
        return second
        