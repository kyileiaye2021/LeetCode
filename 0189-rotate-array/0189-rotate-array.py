class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # happy cases
        # nums = [1,2,3], k = 1
        # outputs: [3,1,2]

        # nums = [1, 2], k = 1
        # output: [2,1]

        # edge cases
        # nums = [1], k = 1
        # output: [1]

        # nums = [1,2,3], k = 3
        # output: [1,2,3]

        # swap the ele in the list
        # split the list into i to k and k+1 to j
        # for the first k ele
        #   swap the ele again to get in order
        # for the second n - k ele
        #   swap the ele again to get in order

        if k == 0:
            return nums

        if k > len(nums):
            k = k % len(nums)

        i = 0
        j = len(nums) - 1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        i = 0
        j = k - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


        i = k
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1





        