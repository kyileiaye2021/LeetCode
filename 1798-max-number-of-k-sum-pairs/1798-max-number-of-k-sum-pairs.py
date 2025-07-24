class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # [1, 3, 3,3, 4]

        # [0, 3, 3], k = 3
        # output: 1

        # sort the arr
        # using two pointers find the nums that add up to sum
        # count the operations

        # [2], k =1
        # output: 0

        # nums = [1,2], k = 5
        # output: 0

        nums.sort()

        count = 0

        l, r = 0, len(nums) - 1

        while l < r:

            curr_sum = nums[l] + nums[r]
            if curr_sum == k:
                count += 1
                l += 1
                r -= 1

            elif curr_sum > k:
                r -= 1

            else:
                l += 1

        return count



            



        