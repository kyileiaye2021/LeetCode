class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Binary Search Algo
        first = self.search_first_occurence(nums, target)
        last = self.search_last_occurence(nums, target)
        return [first, last]
    
    def search_first_occurence(self, nums, target):
        result = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result 
        
        
    def search_last_occurence(self, nums, target):
        result = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result 
            
        
        
        