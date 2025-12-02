class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # max product => to maintain the max product of sub arr
        # curr product => 1
        # iterate thru the nums
        #   multiply curr product with curr nums
        #   update max product if curr product is > max product
        #   check if curr product becomes neg
        #       reset curr product to 1
        # return max product
        # max_product = float('-inf')
        # curr_product = 1
        # for n in nums:
        #     curr_product = curr_product * n
        #     max_product = max(max_product, curr_product, n)
        # return max_product

        currMin = 1
        currMax = 1
        max_product = max(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                currMin = 1
                currMax = 1
                continue
            
            temp = currMax
            currMax = max(currMax * nums[i], currMin * nums[i], nums[i])
            currMin = min(temp * nums[i], currMin * nums[i], nums[i])

            max_product = max(max_product, currMax)

        return max_product
