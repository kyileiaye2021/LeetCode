class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # input: nums = [2,3,1,1,4]
        # output: true

        # input: nums = [1,2,0,0,1]
        # output: false

        # input: nums = [1,1,1,1]
        # output: true

        # input: nums = [3,2,1,0]
        # output: true

        # input: nums = [3,2,1,0,4]
        # output: false


        # input: nums = [0, 2, 1,2]
        # output: false

        # input: nums = [1,0,1,0]
        # output: false

        # input: nums = [3,3,1,0,4]
        # output: true

        # input: nums=[0]
        # output: true

        # input: nums = [1]
        # output: true

        # if index 0 ele is 0 --> return false
        # two pointer
        remaining = 0
        for n in range(len(nums)):
            print(f"n: {n}")
            if remaining < 0:
                return False
            elif nums[n] > remaining:
                remaining = nums[n]
            remaining -= 1
            print(f"remaining: {remaining}")
        return True

