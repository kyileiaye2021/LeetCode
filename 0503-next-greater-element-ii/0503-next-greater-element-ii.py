class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        # N = len(nums)
        # duplicate the nums and add them to nums
        # res = [-1] * 2N
        # iterate thru new nums
        #   while stack and stack[-1] < curr new num
        #       ele, i = pop the stack 
        #       res[i] = curr new num
        #   add the curr new num to stack

        # return res[:N]

        N = len(nums)
        new_nums = nums + nums
        res = [-1] * len(new_nums)
        stack = []

        for i, n in enumerate(new_nums):
            while stack and stack[-1][0] < n:
                ele, idx = stack.pop()
                res[idx] = n

            stack.append((n, i))

        return res[:N]
        