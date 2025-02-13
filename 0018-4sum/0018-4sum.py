class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # based on three sum
        # we used two pointer approach with O(n^2)

        # [-2,-1,0,0,1,2]
        # two pointer with (O(n^3))

        # res list
        # sort the array first 
        # iterate thru the list
        #   a + b + c + d = target
        #   diff = target - d
        #   iterate thru the list 
        #       target = diff - curr val
        #       l, r two pointers
        #       if the l, r ele adding up greater than the target,
        #           shift the r one
        #       elif it is less than the target,
        #           shift the l one
        #       else:
        #           create a list and add it to the res if it is not already in the res list
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            three_sum = target - nums[i]

            for j in range(i + 1, len(nums)):

                two_sum = three_sum - nums[j]

                l,r = j + 1, len(nums)-1

                while l < r:

                    if nums[l] + nums[r] > two_sum:
                        r -= 1
                    
                    elif nums[l] + nums[r] < two_sum:
                        l += 1

                    else:
                        curr_lst = [nums[l], nums[r], nums[j], nums[i]]
                        if curr_lst not in res:
                            res.append(curr_lst)

                        l += 1
                        r -= 1
        return res