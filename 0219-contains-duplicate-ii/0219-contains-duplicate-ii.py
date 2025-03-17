class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Happy case
        # input: nums = [1,2,1], k = 3
        # output: true

        # input: nums = [1,1,1,1], k = 1
        # output: true

        # Edge case
        # input: nums == [-1,0, 2, -1], k = 4
        # output: true

        # input: nums=[1], k = 1
        # output: false

        # input: nums=[1,0,1,5], k = 0
        # output: false

        # Brute Force - O(n^2)
        # Slding Window with fixed k size
        
        # low level plan
        # iterate thru the list until len(list) - k
        #   check the duplicates in the window
        #   if there are duplicates
        #       get index diff 
        #       check if the diff is <= k
        #           return true
        # return false

        if k <= 0:
            return False

        duplicates = set()
        for i, ele in enumerate(nums):
            if ele not in duplicates:
                duplicates.add(ele)

            else:
                return True

            if len(duplicates) > k:
                duplicates.remove(nums[i - k])

        return False


        # for i in range(len(nums) - k):
            
        #     end = i + k + 1
        #     duplicates = set()
        #     # iterate thru fixed window size
        #     for j in range(i, end):
        #         end = j + k + 1
        #         for m in range(j + 1, end):

        #             if nums[m] in duplicates:
        #                 return True

        # return False

