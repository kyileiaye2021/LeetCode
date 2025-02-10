class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # prefix and postfix 

        # given array, create prefix and postfix technique
        # iterate two passes of the array from left to right and right to left
        # keep track of prefix and postfix product vals
        # update the curr ele of nums with its product of prefix and postfix vals

        # Time - O(n)
        # Space - O(n)

        prefix = 1
        postfix = 1

        # creating prefix array
        prefix_arr = [0] * len(nums) 
        for i in range(len(nums)):
            prefix_arr[i] = prefix * nums[i]
            prefix = prefix_arr[i]

        # creating postfix array
        postfix_arr = [0] * len(nums)
        for i in range(len(nums) - 1, 0, -1):
            postfix_arr[i] = postfix * nums[i]
            postfix = postfix_arr[i]

        # updating the nums array with the product of values
        for i in range(len(nums)):

            if i != 0 and i != len(nums) - 1:
                nums[i] = prefix_arr[i - 1] * postfix_arr[i + 1]

            elif i == 0:
                nums[i] = postfix_arr[i + 1]

            else:
                nums[i] = prefix_arr[i - 1]

        return nums

        # using division operation (just try this but not allowed to use in code)
        # Time - O(n)
        # Space - O(n)
        total = 1
        count_zero = 0
        for ele in nums: 
            if ele != 0:
                total *= ele
            else:
                count_zero += 1

        res = []
        for ele in nums:
            if count_zero > 1:
                res.append(0)

            elif count_zero == 1:
                if ele != 0:
                    res.append(0)
                else:
                    res.append(total)
            
            else:
                res.append(total // ele)

        return res
