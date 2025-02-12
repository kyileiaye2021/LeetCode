class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # happy case
        # nums = [1,2, -1]
        # output = 6

        # edge case
        # nums = [1,0]
        # output = 1

        # nums = [-1,0,-2]
        # output = 0

        # brute approach O(n^2)
        # sliding window with two pointers 

        # a var to keep track of max product
        # prev_window_product = 1
        # iterate thru each ele in the list
        #   check if the prev_window_product  is less than 0:
        #       reset it to 1
        #   product the curr ele with prev_window_product and update it
        #   update max product

        # return max product

        # we need to keep track of currMin and currMax because of the negative numbers

        # max_product = nums[0]
        # currMin = 1
        # currMax = 1

        # for i in range(len(nums)):

        #     tmp = currMin 
        #     currMin = min(currMin * nums[i], currMax * nums[i], nums[i])
        #     currMax = max(tmp * nums[i], currMax * nums[i], nums[i])
        #     max_product = max(currMin, currMax, max_product)

        # return max_product
        # time = O(n)
        # space = O(1)

        # another approach
        left_to_right = 1
        right_to_left = 1
        max_product = nums[0]

        for i in range(len(nums)):
            if left_to_right == 0: # reset the neutral val to start a new subarray
                left_to_right = 1

            left_to_right *= nums[i]
            max_product = max(max_product, left_to_right)

        for i in range(len(nums)-1, -1, -1):
            if right_to_left == 0:
                right_to_left = 1

            right_to_left *= nums[i]
            max_product = max(max_product, right_to_left)

        return max_product