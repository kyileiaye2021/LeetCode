class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # space - O(n)
        # time - O(3n)
        # prefix = [1] * len(nums)
        # postfix = [1] * len(nums)

        # # [1,1,2,6]
        # # [1,-1,-1,0,0]
        # pre_product = 1
        # for i in range(len(nums)):
        #     prefix[i] = pre_product
        #     pre_product *= nums[i]

        # # [24,12,4,1]
        # # [0,0,-9,3,1]
        # post_product = 1
        # for i in range(len(nums)-1, -1, -1):
        #     postfix[i] = post_product
        #     post_product *= nums[i]

        # # [24, 12,8,6]
        # for i in range(len(prefix)):
        #     nums[i] = prefix[i] * postfix[i]

        # return nums

        # Space complexity O(1)

        res = [1] * len(nums)
        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
            



