class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # edge cases
        # [8, 2, 0, 6]
        # 1

        # [0,0,0,0]
        # 1

        # []
        # 0

        # [9,9,7,7]
        # 1

        # convert nums to set
        # iteraet thru the nums
        #   check if n - 1 is in nums
        #       continue
        #   cur_len = 1
        #   tmp = n
        #   while tmp + 1 in nums
        #       cur_len += 1
        #       tmp += 1
        #   max_len = max(max len, cur len)
        # return max len

        nums = set(nums)
        max_len = 0

        for n in nums:
            if n - 1 in nums:
                continue

            cur_len = 1
            tmp = n
            while tmp + 1 in nums:
                cur_len += 1
                tmp += 1

            max_len = max(max_len, cur_len)

        return max_len
