class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Happy case
        # input: arr = [1,2,3,4], k = 3, x = 2
        # output: [1,2,3]

        # input: arr = [2,3,3,5], k = 2, x = 3
        # output: [3,3]

        # Edge case
        # input: arr = [1], k = 1, x = 2
        # output: [1]

        # input: arr = [1,1,2,3,4,5], k = 4, x = -1
        # output: [1,1,2,3]

        # Brute Force [O(n) time, O(n)space]
        # - we can use queue
        # - iterate thru the list
        # - add the elements to the queue until the size of the queue is greater than k
        # - when the size of queue is greater than k, 
        # - check if the diff between curr ele and x is greater than that between the ele poped from the queue
        #   - return the curr list
        # - otherwise, 
        #   - we have to pop the ele out and add the curr ele in 

        # Sliding Window 
        # This won't work (linear search)
        # l,r = 0, k-1
        # res list - first k ele
        # increment r by 1
        # iterate thru the list until r passes the len of the list
        #   get the diff1 between curr val and x
        #   get the diff2 between the l ele and x
        #   check if diff1 > diff2:
        #       return the res 
        #   else:
        #       exclude the l ele from the list
        #       add the curr ele to the list
        # return res list

        
        # Use sliding window with a binary search 
        # l,r 
        # we are iterating the whole window thru the list with a binary search
        # l will start at 0
        # r will be at the len(list) - k to maintain k-sized window
        # until l passes r
        #   find the mid index
        #   get the diff between mid val and x (diff1)
        #   get the diff between mid + k val and x (diff2)
        #   check if (diff2) < diff1:
        #       increment l to mid + 1
        #   else:
        #       move r to mid
        # return arr[l:l+ k]

        l, r = 0, len(arr) - k
        while l < r:
            mid = (l + r) // 2
            diff1 = x - arr[mid] 
            diff2 = arr[mid + k] - x

            if diff2 < diff1:
                l = mid + 1
            else:
                r = mid

        return arr[l : l + k]