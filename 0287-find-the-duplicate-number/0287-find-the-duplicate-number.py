class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # hash set
        # O(N) space
        
        # brute force
        # O(n^2) time

        # sorting and check the continuous ele
        # O(nlogn) time
        
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        print(fast)
        temp = nums[0]

        while temp != fast:
            temp = nums[temp]
            fast = nums[fast]
        
        return temp


    