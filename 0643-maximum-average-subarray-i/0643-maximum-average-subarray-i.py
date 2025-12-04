class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # total 
        # keep track of the max avg val
        # combine first 4 ele and get avg
        # iterate thru the ele from the 5th ele 
        #   add the curr ele to total
        #   remove the i - k - 1 ele from the total
        #   calculate the avgg
        #   update the max avg if needed
        # return max avg

        total = 0
        total = sum(nums[:k])
        max_avg = total / k

        for i in range(k, len(nums)):
            total += nums[i]
            total -= nums[i - k]
            curr_avg = total / k
            max_avg = max(max_avg, curr_avg)

        return max_avg
        