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

        # O(nlogn) time complexity
        # O(1) space complexity

        # nums.sort()

        # count = 0

        # l, r = 0, len(nums) - 1

        # while l < r:

        #     curr_sum = nums[l] + nums[r]
        #     if curr_sum == k:
        #         count += 1
        #         l += 1
        #         r -= 1

        #     elif curr_sum > k:
        #         r -= 1

        #     else:
        #         l += 1

        # return count

        count = 0
        freq_map = {}

        for ele in nums:

            diff = k - ele
            if diff in freq_map and freq_map[diff] > 0:

                freq_map[diff] -= 1
                count += 1

            else:
                freq_map[ele] = freq_map.get(ele, 0) + 1

        return count



            



        