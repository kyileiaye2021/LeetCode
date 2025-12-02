class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # when sub array sum becomes neg, set it 0
        # max sum = min num
        # iterate thru the nums
        #   add the curr ele to curr sum 
        #   update the max sum with curr sum if curr sum > max sum
        #   check if max sum < 0
        #       reset max sum to 0
        # return max sum

        max_sum = float('-inf')
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
            print(max_sum)
            if curr_sum < 0:
                curr_sum = 0

        return max_sum

            


      