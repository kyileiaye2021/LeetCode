class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # brute force - O(n^k)
        # want max score
        # max sum of subseq * max num 
        
        # sort the nums2 keeping tracking of index
        # max heap for the nums2 [(ele, index)]
        # iterate thru k times
        #   pop the ele from nums2 and get the indx
        #   get the ele of that index from nums1
        #   add to total
        # find the total / last pop ele

        max_heap = []
        # sorting n2 ele to find the min among max ele 
        for i in range(len(nums2)):
            max_heap.append((-nums2[i], nums1[i]))

        heapq.heapify(max_heap)

        res = 0
        min_heap = [] # [(nums1, num2)]
        total = 0

        # use min_heap to get rid of smallest n1 to get highest multiply score
        for i in range(len(nums1)):
    
            n2, n1 = heapq.heappop(max_heap)
            heapq.heappush(min_heap, n1)
            total += n1

            if len(min_heap) > k:
                n1 = heapq.heappop(min_heap)
                total -= n1

            if len(min_heap) == k:
                res = max(res, (total * -n2))

        return res
