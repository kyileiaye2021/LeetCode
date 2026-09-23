class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:

        #mhappy cases
        # nums = [7,2,5,10,8], k = 2
        # 18

        # nums = [1,2,3,4,5], k = 2
        # 9

        # edge cases
        # nums = [1,2,3,4,5,6], k = 3
        # 9

        # nums = [4], k = 2
        # 4

        # nums = [1,2,3,4,5,6], k = 1
        # 21
        
        # possible range of largest sum subarray
        # smallest= max(nums)
        # largetst = sum(nums)
        l = max(nums)
        r = sum(nums)
        res = 0

        def canSplit(largest):
            total = 0
            subArr = 0
            for n in nums:
                total += n

                if total > largest:
                    subArr += 1
                    total = n

            return True if subArr + 1 <= k else False


        while l <= r:
            mid = (l + r) // 2

            if canSplit(mid):
                res = mid
                r = mid - 1
                
            else: 
                l = mid + 1

        return res



