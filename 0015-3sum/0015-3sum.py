class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the list
        # iterate thru the list
        #   two pointers l, r
        #   l = i + 1
        #   r = end of the list
        #   while l < r
        #       check if the l ele + r ele + curr ele > 0
        #           decrement r
        #       elif < 0
        #           increment l
        #       else:
        #           add the ele triplet in the list
        #           decrement r and increment l

        nums.sort()
        res = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                if (nums[l] + nums[r] + nums[i]) > 0:
                    r -= 1

                elif (nums[l] + nums[r] + nums[i]) < 0:
                    l += 1

                else:
                    curr_list = [nums[i], nums[l], nums[r]]
                    res.append(curr_list)
                    l += 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
