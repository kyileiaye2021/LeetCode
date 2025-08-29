class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums = [1,2,3], k = 3
        # output: [1, 2, 3]
        # two pointers
        # i, j = len(nums) - 1
        # create an arr of size k
        # iterate thru the nums from the last until j < 0
        #   if k > 0
        #       store the ele in the arr
        #   else:
        #       assign the ele to the i
        #       decrement i 
        #   decrement j

        # iterate thru arr from the last
        #   put the ele to i 
        #   decrement i

        # first reverse the whole array
        # there are two portions in the arr: [0: k-1 and k up to last ele]
        # original - [1,2,3,4,5], k = 3
        #  [1,2 | 3, 4, 5]
        #  [5, 4, 3, 2, 1]
        #  [5, 4, 3 | 2, 1]
        #  [3, 4, 5 | 1, 2]
        # reverse the entire array with two pointers
        # reverse the first portion [0 : k - 1]
        # reverse the second portion [k : len(nums)]
        # edge cases
        # k > len(nums) --> k = k % len(nums)

        k = k % len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            