class Solution:
    def jump(self, nums: List[int]) -> int:

        # bfs
        res = 0
        l = 0
        r = 0

        while r < len(nums) - 1:
            # find the furthest we can reach from the curr point
            furthest = 0

            for i in range(l, r + 1):
                furthest = max(furthest, nums[i] + i)
            
            l = r + 1
            r = furthest
            res += 1
        return res
        