class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Happy cases
        # input - nums = [2,7,11,15], target = 9
        # output - [0, 1]
        
        # Edge cases
        # input - nums = [3,3], target = 6
        # output - [0,1]
        
        # Hashmap Approach
        # create a hashmap
        # iterate over the list
        #   check if the subtraction of curr ele from the target is in the hashmap
        #       make a list of the curr ele index and the val of the hashmap and return
        # add the curr ele to the hashmap with its index
        
        # Time complexity - O(n)
        # Space complexity - O(n)
        
        hashmap = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff],i]
            
            else:
                hashmap[nums[i]] = i
                
        