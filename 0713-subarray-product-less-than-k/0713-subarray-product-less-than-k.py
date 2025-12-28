class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # two pointer sliding window
        # total_product
        # count 
        # l , r
        # iterate thru the ele until r reach the end
        #   if curr < k 
        #       increment count by 1
        #       multiply total with curr
        #       check if total < k
        #           increment count by 1
        #       else
        #           divide the total by l ele
        #           increment l 
        # return count

        # [10, 50, 100, 600]
        # [10, 60, 12, 6]

        total_product = 1
        count = 0
        l = 0
        r = 0
        while r < len(nums):
            total_product *= nums[r]

            while l <= r and total_product >= k:
                total_product = total_product // nums[l]
                l += 1
            count += r - l + 1 
            r += 1
        return count

        
            

