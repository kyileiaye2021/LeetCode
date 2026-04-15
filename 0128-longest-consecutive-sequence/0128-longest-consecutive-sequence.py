class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        nums = set(nums)
        for n in nums:
            # start of subseq
            if n - 1 not in nums:
                cur_len = 1
                start = n
                while start + 1 in nums:
                    cur_len += 1
                    start = start + 1

                max_len = max(cur_len, max_len)

        return max_len


        