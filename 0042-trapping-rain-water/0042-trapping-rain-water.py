class Solution:
    def trap(self, height: List[int]) -> int:
        # happy case
        # input: height = [1,0,1]
        # output: 1

        # input: height = [0, 2, 1, 0, 2]
        # output: 3

        # input: height = [0, 1, 0, 1, 0]
        # output: 1

        # input: height = [1, 0, 0, 0, 1]
        # output: 3

        # edge cases
        # input: [0,0,0,0]
        # output; 0

        # input: [0,1,0]
        # output: 0

        # input: [1]
        # output: 0

        # on the left and right side, we need to keep track of the longest bar
        # we have l and r pointers at the end
        # we get the min of left and right pointers
        # do min-l_ele and min - r_ele
        # if min-l_ele > 0: add it to the total
        # if min-r_ele > 0: add it to the total
        # update the min

        # first thing - we have to get the max left and max right
        # second - we have to get the min of max_left and max_right
        # n = len(height)
        # max_left = [0] * n
        # max_right = [0] * n
        # min_num = [0] * n

        # curr_l = 0
        # for i, h in enumerate(height):
        #     max_left[i] = curr_l
        #     curr_l = max(curr_l, height[i])

        # curr_r = 0
        # for i in range(n-1, -1, -1):
        #     max_right[i] = curr_r
        #     curr_r = max(curr_r, height[i])

        # for i in range(n):
        #     min_num[i] = min(max_left[i], max_right[i])

        # res = 0
        # for i, h in enumerate(height):
        #     if (min_num[i] - h) > 0:
        #         res += min_num[i] - h

        # return res

        l, r = 0, len(height) - 1
        max_left = height[l]
        max_right = height[r]

        res = 0
        while l < r:
            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                res += (max_left - height[l])
                
            else:
                r -= 1
                max_right = max(max_right, height[r])
                res += (max_right - height[r])

        return res




