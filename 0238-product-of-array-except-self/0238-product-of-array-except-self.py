class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums: [1,2,3,4]
        # prefix: [1, 1, 2, 6]
        # postfix: [24,12, 4, 1]
        # iterate thru the prefix and postfix
        #   multiply at each position
        
        prefix = [1] * len(nums)
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        postfix = [1] * len(nums)
        for i in range(len(postfix) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        res = []
        for i, n in enumerate(prefix):
            res.append(n * postfix[i])
        return res



