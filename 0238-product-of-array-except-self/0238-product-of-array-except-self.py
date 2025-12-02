class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix_product = [1] * (len(nums) + 1)
        postfix_product = [1] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix_product[i + 1] = prefix_product[i] * nums[i]

        for i in range(len(nums) -1, -1, -1):
            postfix_product[i] = postfix_product[i + 1] * nums[i]

        for i in range(len(nums)):
            res.append(prefix_product[i] * postfix_product[i + 1])

        return res
        