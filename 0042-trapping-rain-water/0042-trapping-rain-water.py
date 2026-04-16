class Solution:
    def trap(self, height: List[int]) -> int:

        # prefix = [0] * len(height)
        # for i in range(1, len(height)):
        #     prefix[i] = max(height[i - 1], prefix[i - 1])

        # postfix = [0] * len(height)
        # for i in range(len(height) - 2, -1, -1):
        #     postfix[i] = max(height[i + 1], postfix[i + 1])

        # res = 0
        # for i in range(len(height)):
        #     boundary = min(prefix[i], postfix[i])
        #     water = boundary - height[i]
        #     if water > 0:
        #         res += water

        # return res

        # res = [0] * len(height)
        # for i in range(1, len(height)):
        #     res[i] = max(height[i - 1], res[i - 1])

        # postfix = 0
        # for i in range(len(height) - 1, -1, -1):
        #     boundary = min(res[i], postfix)
        #     water =  boundary - height[i]
        #     if water > 0:
        #         res[i] = water
        #     else:
        #         res[i] = 0
            
        #     postfix = max(height[i], postfix)

        # return sum(res)

        maxL = height[0]
        maxR = height[-1]
        res = 0

        l = 0
        r = len(height) - 1

        while l < r:
            if maxL < maxR:
                l += 1
                water = max(0, maxL - height[l])
                maxL = max(maxL, height[l])

            else:
                r -= 1
                water = max(0, maxR - height[r])
                maxR = max(maxR, height[r])

            res += water

        return res

        