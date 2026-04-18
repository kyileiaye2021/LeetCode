class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # brute force
        # sort - O(nlogn)
        # fast slow pointer

        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        temp = 0
        while True:
            temp = nums[temp]
            slow = nums[slow]

            if temp == slow:
                break
        return slow

