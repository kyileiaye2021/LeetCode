class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # two pointer technique
        # keep track of the bool val (skip)

        # nums = [1,1,1,2,2,3]

        # nums = [1, 2, 2, 3]

        # l, r = 1, 1
        # iterate thru the nums until the r is > len(nums)
        #   check if the r ele is equal to r - 1
        #       check if skip is false
        #           move l and r by 1
        #       else:
        #           move r by 1
        #   else:
        #       reassign the skip to False
        #       move r by 1

        l, r = 1, 1
        skip = False
        while r < len(nums):

            if nums[r] == nums[r - 1]:
                if not skip:
                    skip = True
                    nums[l] = nums[r]
                    l += 1
            else: 
                skip = False
                nums[l] = nums[r]
                l += 1

            r += 1
            
        return l




