class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # curr window
        # 1,3,-1 max = 3
        # 3,-1,1
        # if chopped ele ->not max => compare the max with the curr ele
        # else find max among the window

        # res = []
        # cur_max = max(nums[:k])
        # res.append(cur_max)
        # l = 0

        # for r in range(k, len(nums)):
        #     chopped = nums[l]
        #     l += 1
        #     if chopped != cur_max:
        #         cur_max = max(cur_max, nums[r])
        #     else:
        #         cur_max = max(nums[l:r + 1])
        #     res.append(cur_max)

        # return res

        dq = deque()
        l = 0
        res = []

        for r, n in enumerate(nums):
            # while adding remove the smaller ele bc those are not important
            while dq and nums[dq[-1]] < n:
                dq.pop()

            dq.append(r)

            # shrink the window first bc sometimes we may take the one that can be outside the curr window
            if l > dq[0]:
                dq.popleft()
                
            # if there is a valid window
            if r + 1 >= k:
                idx = dq[0]
                res.append(nums[idx])
                l += 1
            
        return res
