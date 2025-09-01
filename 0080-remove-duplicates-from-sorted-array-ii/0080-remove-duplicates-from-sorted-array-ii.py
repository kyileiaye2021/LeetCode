class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # two pointer
        # bool var to keep track of the ele appears twice or not
        # found = bool var false
        # i , j 
        # iterate the nums with j 
        #   check if j ele == j - 1 ele
        #       if found is false
        #           set found to true
        #           move i by 1
        #          
        #  else:
        #      assign j ele to i
        #      move i by 1
    
        #  move j by 1
        # return i 

        i, j = 1, 1
        found = False
        while j < len(nums):
            if nums[j] == nums[j - 1]:
                if not found:
                    found = True
                    nums[i] = nums[j]
                    i += 1

            else:
                found = False
                nums[i] = nums[j]
                i += 1

            j += 1

        return i
