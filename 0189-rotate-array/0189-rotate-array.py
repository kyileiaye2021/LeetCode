class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Space - O(1)
        # happy cases
        # input: nums = [1,2,3], k = 1
        # output: [3,1,2]

        # edge case:
        # input: nums = [1,2,3], k = 0
        # output: [1,2,3]


        # two pointers
        # brute force - shifting the elements of size k to the right'
        # reversing the array - reverse the whole array and reverse first k elements and then remaining elements

        k = k % len(nums)
        l,r = 0, len(nums) - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        l,r = 0, k - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        l,r = k, len(nums) -1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            

            