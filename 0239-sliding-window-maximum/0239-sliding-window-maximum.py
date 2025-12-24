class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # O(k * n)
        # find max ele in first k ele
        # add it to the res
        # iterate thru the ele k + 1 ele
        #   remove the i - k ele
        #   add the kth ele and update the max ele
        #   add the max ele to the res
        # return res
        
        # res = []
        # max_ele = max(nums[:k])
        # res.append(max_ele)
        # print('First ele: ', res)

        # for i in range(k, len(nums)):
        #     curr_window = nums[i - k + 1: i + 1]
        #     max_ele= max(curr_window)
        #     res.append(max_ele)

        # return res

        # sliding window and deque
        # iterate thru the ele
        #   while curr ele is greater than the last ele of deque
        #       pop the ele out
        #   add the curr ele to the deque
        #   k -= 1
        #   when k == 0:
        #       update the max ele 
        # if l pointer ele is = to first ele of deque
        #   pop out that from deque

        l = 0
        queue = deque()
        res = []

        for r in range(len(nums)):

            # add the ele to the deque 
            while queue and nums[r] > nums[queue[-1]]:
                queue.pop()
            
            queue.append(r)

            # remove left ele if they are out of window
            if l > queue[0]:
                queue.popleft()

            # if window size becomes k, get the max elel of the window
            if r >= k - 1:
                res.append(nums[queue[0]])
                l += 1


        return res


    

            

        
        