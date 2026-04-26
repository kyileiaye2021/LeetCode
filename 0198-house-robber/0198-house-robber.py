class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[-1]
        total_money = [0] * len(nums)
        total_money[0] = nums[0]
        total_money[1] = max(total_money[0], nums[1])


        for i in range(2, len(nums)):
            if nums[i] + total_money[i - 2] > total_money[i - 1]:
                total_money[i] = nums[i] + total_money[i - 2]
            
            else:
                total_money[i] = total_money[i - 1]
        
        print(total_money)
        return total_money[-1]
        