class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # iterate thru the quaries
        # idx 1, idx 2
        # iterate from idx 1to idx 2
        #   decrement the ele by 1 in these indices of the nums arr

        # iterate thru the ele in the nums
        #   check if the curr not 0
        #       return false
        # return true

        # for idx1, idx2 in queries:
        #     for i in range(idx1, idx2 + 1):
        #         if nums[i] > 0:
        #             nums[i] -= 1

        # for n in nums:
        #     if n != 0:
        #         return False

        # return True

        # create an arry to store the ranges of start and end ele
        # accumulate the prefix sum to get the right num of operations 
        # if the num of operations > = curr nums:
        #   good to go

        temp = [0] * (len(nums) + 1)

        for start, end in queries:
            temp[start] += 1
            temp[end + 1] += -1

        for i in range(1, len(temp)):
            temp[i] += temp[i-1]

        for i in range(len(nums)):
            if nums[i] > temp[i]:
                return False
        
        return True

        
