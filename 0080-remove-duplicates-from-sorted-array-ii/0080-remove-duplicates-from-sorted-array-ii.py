class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        # i, j = 1, 1
        # k = 0
        # while j < len(nums)
        #   if j ele == j - 1 ele
        #       if k <= 1:
        #           i += 1
        #           j += 1
        #           k += 1
        #       else: j += 1
        #   else
        #       i ele = j ele
        #       i +=1
        #       j += 1
        # return i

        i = 1
        j = 1
        k = 1

        while j < len(nums):
            if nums[j] == nums[j - 1]:
                if k <= 1:
                    nums[i] = nums[j]
                    i += 1
                    k += 1

            else:
                nums[i] = nums[j]
                i += 1
                k = 1

            j += 1

        return i
                