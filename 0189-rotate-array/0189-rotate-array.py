class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums = [-1, -100, 3, 99]
        # k = 2
        # output: [3, 9, -1, -100]

        # nums = [-1, -100, 3, 99]
        # k = 15
        # [99, -1, 100, 3]
        # [3, 99, -1, 100]
        # [-100, 3, 99, -1] <--
        # [-1, -100, 3, 99]
        # [99, -1, 100, 3]
        # mod k by len of nums

        # [99, 3, -100, -1]
        # [-100, 3, 99, -1]

        # k = 3
        # swapping with 2 pointers
        # i, j
        # reverse the list
        #   swap i and j ele
        # for the 1st k portion 
        #   reverse the list
        # for the rest of the portion
        #   reverse the list

        n = len(nums)
        k = k % n

        i, j = 0, n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        i, j = 0, k - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        i, j = k, n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        