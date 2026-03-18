class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        #  i = 1, j = largest ele in nums
        #  iterate i from 1 to largest ele in nums
        #   mid = i + j // 2
        #   total = 0
        #   iterate thru the ele
        #       res = divide the curr ele by mid (ceil)
        #       total += res
        #   if total == threshold
        #       return mid
        #   elif total > threshold
        #       i = mid + 1
        #   else:
        #       i = mid - 1

        i = 1 
        j = max(nums)
        res = 0

        while i <= j:
            mid = (i + j) // 2
            total = 0

            for k in nums:
                total += ceil(k / mid)
            
            if total <= threshold:
                res = mid
                j = mid - 1
            else:
                i = mid + 1

        
        return res

