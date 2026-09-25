class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # sort the arr - O(nlogn)

        # set - O(n) space

        # slow and fast pointer
        # slow = 0
        # fast = 0

        # while True:
        #   slow = arr[slow]
        #   fast = arr[arr[fast]]
        #   if slow == fast:
        #       return nums[slow]
        # slow = 0
        # while slow != fast:
        #   slow = arr[slow]
        #   fast = arr[fast]
        # return slow

        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow