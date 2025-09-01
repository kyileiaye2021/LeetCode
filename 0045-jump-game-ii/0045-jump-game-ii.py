class Solution:
    def jump(self, nums: List[int]) -> int:
        # increment the count when replacing the amount
        # increament the count 1 time when decrementing the remaining
        # nums = [2,3,1,1,4,5]
        # output: 3
        # nums = [2,3,4,5]
        # output: 2

        # BFS on 1D array
        # start from index 0 ele
        # in each step or layer, we have to go farthest (right) and current step + 1 (left)
        # left and right --> window or layer size

        # l and r pointers starting from 0s
        # step num
        # iterate thru the list with r
        #   the farthest will be reset to 0 in each layer
        #   l pointer will be current + 1
        #   r pointer will be at the pos where the ele in the layer can go to the farthest pos
        #   incrementing our step num

        l, r = 0, 0
        steps = 0

        while r < len(nums) - 1: # we need to stop when we reach last index
            # for each layer, we are reseting the farthest to 0 
            farthest = 0

            # iterating thru the elements in each layer
            for i in range(l, r + 1):
                # finding the farthest pos in the next window where each ele in the curr window can go
                farthest = max(farthest, i + nums[i]) 

            l = r + 1
            r = farthest
            steps += 1

        return steps

