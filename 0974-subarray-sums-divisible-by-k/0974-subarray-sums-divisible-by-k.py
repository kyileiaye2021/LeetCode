class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:

        # happy cases
        # nums = [4,5,0,-2,-3,1], k = 5
        # 7

        # nums = [2,1,3], k = 3
        # [2,1,3], [2,1], [3]
        # 3

        # edge cases
        # nums = [2], k = 9
        # 0

        # nums = [2,3,1,0], k = 6
        # 2

        # prefix sum
        # nums = [2,1,3], k = 3
        # [2,3,6]

        # (prefix2 - prefix1) % k == 0
        # prefix2 % k = prefix1 % k

        prefix_rem_count = {0: 1}
        curr_sum = 0
        res = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum % k in prefix_rem_count:
                res += prefix_rem_count[curr_sum % k]

            prefix_rem_count[curr_sum % k] = 1 + prefix_rem_count.get(curr_sum % k, 0)

        return res



        