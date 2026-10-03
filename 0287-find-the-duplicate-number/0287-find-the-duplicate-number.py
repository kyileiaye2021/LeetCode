class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # set O(n) space
        # hashmap
        # sort O(nlogn) time
        # slow and fast  pointer and detect the cycle

        # slow, fast = first ele
        # while true
        #   slow = nums[slow]
        #   fast = nums[nums[fast]]
        #   if slow == fast
        #       break
        # slow = first ele
        # keep moving slow and fast 1 time until they meet

        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow

        