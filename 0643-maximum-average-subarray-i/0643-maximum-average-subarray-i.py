class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # nums = [1,2,3,4], k = 4
        # avg = 1+2+3+4/4 =10/4 = 2.5

        max_avg = float('-inf')
        j = 0
        avg = sum(nums[j:k])/k
        max_avg = max(max_avg, avg)
    
        for i in range(k, len(nums)):
            j += 1
            avg = sum(nums[j:i + 1]) / k
            max_avg = max(max_avg, avg)
        
        return max_avg
